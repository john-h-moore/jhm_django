from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
	exclude = ['posted']
	prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)