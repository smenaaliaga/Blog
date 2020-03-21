from django.db import models
from django.utils import timezone

STATUS = (
    (0, "Oculto"),
    (1, "Publicado")
)

class Category(models.Model) :
    category = models.CharField(max_length=200, verbose_name="Categoria")

    class Meta :
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) :
        return self.category

class Post(models.Model) :
    title = models.CharField(max_length=200, verbose_name="Título")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Categoria", 
    help_text="Seleccione categoria")
    content = models.TextField(verbose_name="Contenido")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Fecha publicación")
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Estado")

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    class Meta :
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
    
    def __str__(self) :
        return self.title