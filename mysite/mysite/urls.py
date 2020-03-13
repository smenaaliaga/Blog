from django.contrib import admin
from django.urls import path
from blog.views import home, post, year_posts

urlpatterns = [
    path('', home),
    path('post/<id>', post),
    path('<int:year>/', year_posts),
    path('admin/', admin.site.urls),
]
