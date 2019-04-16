from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Logline
from .utilities import PrettyDiffMatchPatch


class LoglineListView(ListView):
    model = Logline


class LoglineDetailView(DetailView):
    model = Logline


class LoglineCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Logline
    fields = ['title', 'body']
    success_message = 'Logline created successfully.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LoglineUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Logline
    fields = ['title', 'body']
    success_message = 'Logline updated successfully.'


class LoglineHistoryDetailView(DetailView):
    template_name = 'loglines/logline_detail_history.html'

    def get_object(self, queryset=None):
        return Logline.history.get(id=self.kwargs['pk'], history_id=self.kwargs['history_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = Logline.history.filter(history_date__lt=self.object.history_date).count() + 1
        context['diff'] = self.get_diff()
        return context

    def get_diff(self):
        obj = self.get_object()
        if obj.prev_record is not None:
            dmp = PrettyDiffMatchPatch()
            diff = dmp.diff_main(obj.body, obj.prev_record.body)
            dmp.diff_cleanupSemantic(diff)
            return dmp.diff_prettyHtml(diff)
        else:
            return ''
