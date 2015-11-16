from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Item
from .forms import ItemForm


class ItemListView(ListView):
    model = Item
    context_object_name = 'item_list'


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm

    def form_valid(self, form):
        item = form.save(commit=False)
        item.author = self.request.user
        return super(ItemCreateView, self).form_valid(form)
