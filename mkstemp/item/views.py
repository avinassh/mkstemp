from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse


from .models import Item
from .forms import ItemForm


class ItemListView(ListView):
    model = Item
    context_object_name = 'item_list'
    queryset = Item.objects.filter(parent=None)


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['form'] = ItemForm(initial={'parent': self.object})
        context['form'].fields.pop('title')
        context['form'].fields.pop('url')
        return context


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm

    def form_valid(self, form):
        item = form.save(commit=False)
        item.author = self.request.user
        parent = form.cleaned_data.get('parent', None)
        if parent:
            self.success_url = reverse('item-detail', kwargs={'pk': parent.id})
        return super(ItemCreateView, self).form_valid(form)
