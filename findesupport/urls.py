from django.conf.urls import url

from findesupport import views

urlpatterns = [
    url(r'^fin', views.finProduit_list, name='post_list'),
    url(r'^produit/new/$', views.produit_new, name='produit_new'),
]