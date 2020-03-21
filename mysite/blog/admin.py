from django.contrib import admin

from .models import Post, Category

admin.site.register(Category)
# admin.site.register(Post)

# Define the admin class
class PostAdmin(admin.ModelAdmin) :
    list_display = ('title', 'published_date', 'status')
    list_filter = ('published_date', 'status')

# Register the admin class with the associated model
admin.site.register(Post, PostAdmin)