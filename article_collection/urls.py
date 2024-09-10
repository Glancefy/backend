from django.urls import path
from .views import hello_article_collection

urlpatterns = [
    path("hello/", hello_article_collection, name="hello_world"),
]
