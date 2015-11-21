from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.http import Http404


from mkstemp.item.models import Item
from .models import Report


class ReportListView(ListView):
    model = Report
    context_object_name = 'report_list'
    queryset = Report.objects.filter(resolved=False)


class ReportCreateView(CreateView):
    model = Report
    success_url = '/report/'
    fields = ['text']

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = self.request.user
        report.item = self._get_item_from_query_param()
        return super(ReportCreateView, self).form_valid(form)

    def _get_item_from_query_param(self):
        try:
            return get_object_or_404(Item, pk=int(self.request.GET.get('id')))
        except (ValueError, TypeError):
            raise Http404('No Item matches the given query.')
