from django.urls import path
from .views import (
    BlogListView,BlogDetailView,BlogCreateView,BlogEditView,BlogDeleteView
)

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('post/new/',BlogCreateView.as_view(), name='new_post'),
    path('post/<int:pk>/edit/',BlogEditView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='post_del')
]