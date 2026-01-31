
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='homepage'),
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    



    path("__reload__/", include("django_browser_reload.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
