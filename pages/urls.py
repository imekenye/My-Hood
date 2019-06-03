from django.urls import path
from .views import PostDetailView, PostCreateView, PostUpdateView,PostListView
from . import views

urlpatterns = [

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostUpdateView.as_view(), name='post-delete'),
    path('post/new', PostCreateView.as_view(), name='post-create'),

]
