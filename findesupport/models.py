from django.db import models


class Editeur(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Produit(models.Model):
    nom = models.CharField(max_length=200)
    nom_editeur = models.ForeignKey('findesupport.Editeur')
    datefds = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text
