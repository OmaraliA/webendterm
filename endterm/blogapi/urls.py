from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name = "post_list"),
    path('posts/<int:post_id>/', views.post_details, name='post_details'),
]
