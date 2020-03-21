from django.contrib import admin
from django.urls import path
from blog.views import home, year_posts, month_posts, detail_posts

urlpatterns = [
    path('', home),
    path('<int:year>/', year_posts),
    path('<int:year>/<int:month>/', month_posts),
    path('<int:year>/<int:month>/<id>/', detail_posts),
    path('skynet/', admin.site.urls),
]
