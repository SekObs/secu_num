from django.shortcuts import render, redirect

from findesupport.models import Produit
from findesupport.forms import ProduitForm

def finProduit_list(request):
    produits = Produit.objects.filter('nom')
    return render(request, 'findesupport/support_list.html', {'produits': produits})

def produit_new(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            produit = form.save(commit=False)
            produit.author = request.user

            produit.save()
            return redirect('produit_detail', pk=produit.pk)
    else:
        form = ProduitForm()
    return render(request, 'findesupport/produit_edit.html', {'form': form})