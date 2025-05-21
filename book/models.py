from django.db import models  # type: ignore


# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    data_publicacao = models.DateField()
    sinopse = models.TextField()

    def __str__(self):
        return self.titulo