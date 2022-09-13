from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    return render(request, "katalog.html", context)

data_barang_katalog = CatalogItem.objects.all()
context = {
    'list_barang': data_barang_katalog,
    'nama': 'Davina'
}