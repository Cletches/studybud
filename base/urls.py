from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('connect/',views.connect, name="connect"),
    path('projects/',views.projects, name="projects"),  

]
