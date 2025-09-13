from django.db import models
 
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    preço = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

def __str__(self):
    return self.nome