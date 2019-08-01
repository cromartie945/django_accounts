from django.shortcuts import render
from .models import Post
'''
posts = [
    {
       "author":'haynes245',
       'title': 'Blog Post 1',
       'contnt': 'First post content',
       'date_posted':'August 27, of 2017'
    },
    {
       "author":'Jane Doe',
       'title': 'Blog Post 2',
       'contnt': 'Second post content',
       'date_posted':'August 28, of 2017'
    },
]
'''
# Create your views here.
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
