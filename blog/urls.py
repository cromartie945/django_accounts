from django.urls import path
from . import views
#from .views import PostListView,PostDetailView
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    #path('',views.home,name='blog-home')
    path('detail/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/update/<int:pk>/',PostUpdateView.as_view(),name='post-update'),
    path('post/delete/<int:pk>/',PostDeleteView.as_view(),name='post-delete'),
    path('',PostListView.as_view(),name='blog-home'),
    path('about/',views.about,name='blog-about'),
]
