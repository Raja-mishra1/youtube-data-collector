from django.urls import path

from .views import get_video,get_video_all

app_name = "search"

urlpatterns = [
    path("search/<str:title>/", get_video, name="search"),
    path("search_all/",get_video_all, name="search_all"),
]