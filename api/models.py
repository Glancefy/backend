from django.db import models
from django.contrib.postgres.fields import ArrayField


class NewsSource(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(unique=True)
    reliability_score = models.FloatField(default=0.0)
    political_leaning = models.CharField(
        max_length=50,
        choices=[
            ("far_left", "Far Left"),
            ("left", "Left"),
            ("center_left", "Center Left"),
            ("center", "Center"),
            ("center_right", "Center Right"),
            ("right", "Right"),
            ("far_right", "Far Right"),
        ],
    )
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    last_scraped = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField(unique=True)
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    author = models.CharField(max_length=200, blank=True)
    published_date = models.DateTimeField()
    content = models.TextField()
    summary = models.TextField(blank=True)
    keywords = ArrayField(models.CharField(max_length=100), blank=True)
    category = models.CharField(max_length=100)
    sentiment_score = models.FloatField(null=True, blank=True)
    objectivity_score = models.FloatField(null=True, blank=True)
    ai_generated_tags = ArrayField(models.CharField(max_length=100), blank=True)
    read_time = models.IntegerField(help_text="Estimated read time in minutes")

    # Fields for comparative analysis
    related_articles = models.ManyToManyField("self", blank=True)

    # Fields for user interaction
    view_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]
