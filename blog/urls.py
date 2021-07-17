from django.urls import path
from . import views

urlpatterns = [
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('add/', views.add_post, name='add_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
]