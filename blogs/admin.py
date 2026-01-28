from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)


# Register your models here.
from .models import Category, Blog
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)