from django.db import models
from django.utils import timezone

class Post(models.Model) :
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    class Meta :
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
    
    def __str__(self) :
        return self.title