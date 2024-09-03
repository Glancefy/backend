import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery(
    "core",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["article_collection.tasks"],
)


app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
