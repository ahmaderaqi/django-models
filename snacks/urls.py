from django.contrib import admin
from django.urls import path
from .views import HomePageView,AboutPageView,SnackDetailsView,SnacksListView

urlpatterns = [
    
    path('',HomePageView.as_view(), name="home"),
    path('about',AboutPageView.as_view(), name="about"),
    path('things',SnacksListView.as_view(), name="snacks"),
    path('<int:pk>/',SnackDetailsView.as_view(), name="snacks_detail")
]