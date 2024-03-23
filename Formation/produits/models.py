from django.db import models

# Create your models here.
class Produits(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.DecimalField(max_digits=100000, decimal_places=2)



    class Meta:
        verbose_name = ("Poduit")
        verbose_name_plural = ("Poduits")
    

    def __str__(self):
        return self.nom
