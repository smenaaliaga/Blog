from django.db import models
import datetime

class Post(models.Model) :
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    datePost = datetime.datetime.now()
    
    class Meta :
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
    
    def __str__(self) :
        return self.title