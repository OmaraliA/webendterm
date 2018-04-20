from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = "post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/(?P<pk>\d+)/edit/', views.post_edit, name='post_edit'),
    path('post/(?P<pk>\d+)/delete/', views.post_delete, name='post_delete'),
]