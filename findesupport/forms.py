from django import forms

from findesupport.models import Produit


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ('nom', 'datefds',)