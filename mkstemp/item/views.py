from django.views.generic import ListView, DetailView
from .models import Item


class ItemListView(ListView):
    model = Item
    context_object_name = 'item_list'


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
