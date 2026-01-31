from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Category, Blog


def home(request):
  categories = Category.objects.all()
  featured_post = Blog.objects.filter(is_featured=True)
  feature_front = Blog.objects.filter(featured_front=True)
  recent_post = Blog.objects.all()
  context = {
    'categories' : categories,
    'featured_post' : featured_post,
    'feature_front' : feature_front,
    'recent_post' : recent_post,
  }
  return render(request, 'base.html', context)



def posts_by_category(request, category_id):

  posts = Blog.objects.filter(status='1', category= category_id)
  
  context = {
    'posts' : posts,
    

  }
  return render(request, 'category_by_posts.html', context)

# render(request, 'base.html')