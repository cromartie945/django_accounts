from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
class PostListView(ListView):
    model = Post
    template_name='blog/home.html' #<app>/<model>_<view_type>.html
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model = Post
    #template_name='blog/home.html' #<app>/<model>_<view_type>.html
    #context_object_name='posts'
    #ordering=['-date_posted']


class PostCreateView(LoginRequiredMixin, CreateView):
    model =Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    model =Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()      # gets current post
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()      # gets current post
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html',{'title':'About'})
