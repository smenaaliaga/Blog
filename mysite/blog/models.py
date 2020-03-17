from django.db import models
from django.utils import timezone

STATUS = (
    (0, "Hidden"),
    (1, "Published")
)

class Post(models.Model) :
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField(verbose_name="Contenido")
    published_date = models.DateTimeField(
            default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    class Meta :
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
    
    def __str__(self) :
        return self.title

class Category(models.Model) :
    category = models.CharField(max_length=200, verbose_name="Categoria")