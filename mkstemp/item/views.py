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

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['form'] = ItemForm(initial={'parent': self.object})
        return context


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm

    def form_valid(self, form):
        item = form.save(commit=False)
        item.author = self.request.user
        return super(ItemCreateView, self).form_valid(form)
