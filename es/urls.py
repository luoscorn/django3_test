from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from es.views import BookSearchView

router = routers.DefaultRouter()
router.register("book/search", BookSearchView, base_name="book-search")
urlpatterns = [
]
urlpatterns += router.urls