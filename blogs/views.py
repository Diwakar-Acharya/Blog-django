from django.shortcuts import render, redirect
from django.http import HttpResponse

from blogs.models import Category, Blog
from django.shortcuts import get_object_or_404




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
  categories = Category.objects.all()
  try:
    category = Category.objects.get(pk=category_id)
  
  except:
    return redirect('homepage')

  context = {
    'posts' : posts,
    'categories' : categories,
    

  }
  return render(request, 'category_by_posts.html', context)

# render(request, 'base.html')


def blogs(request, slug,):
  categories = Category.objects.all()
  single_blog = get_object_or_404(Blog, slug=slug, status='1')
  detail = Blog.objects.filter(status='1', slug=slug)
  
  context = {
    'single_blog' : single_blog,
    'detail' : detail,
    'categories' : categories,
   
  }
  return render(request, 'blogs.html', context)