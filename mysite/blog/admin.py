from django.contrib import admin

from .models import Post, Category

admin.site.register(Category)
# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin) :
    list_display = ('title', 'published_date', 'status')
    list_filter = ('published_date', 'status')

admin.site.register(Post, PostAdmin)