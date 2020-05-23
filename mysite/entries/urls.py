from django.urls import path
from . import views

# app_name='entries'

urlpatterns = [

    path('show_videos/', views.show_videos, name='show_videos'),

]