from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Item


class ItemListView(ListView):
    model = Item
    context_object_name = 'item_list'


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'


class ItemCreate(CreateView):
    model = Item
    fields = ['title', 'text', 'url']

    def form_valid(self, form):
        item = form.save(commit=False)
        item.author = self.request.user
        return super(ItemCreate, self).form_valid(form)
