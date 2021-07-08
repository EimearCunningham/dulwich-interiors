from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog, name='blog'),
    path('', views.post_detail, name='post_detail'),
]