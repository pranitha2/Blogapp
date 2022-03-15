from . import views
from django.urls import path

urlpatterns = [
    path('homepage/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]