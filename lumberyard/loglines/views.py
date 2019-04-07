from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from reversion.models import Version
from reversion.views import RevisionMixin

from .models import Logline
from .utilities import PrettyDiffMatchPatch


class LoglineListView(ListView):
    model = Logline


class LoglineDetailView(DetailView):
    model = Logline

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['versions'] = Version.objects.get_for_object(self.get_object())
        return context


class LoglineCreateView(LoginRequiredMixin, RevisionMixin, CreateView):
    model = Logline
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LoglineUpdateView(LoginRequiredMixin, RevisionMixin, UpdateView):
    model = Logline
    fields = ['title', 'body']


class VersionDetailView(DetailView):
    model = Version

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        previous_version = self.get_previous_or_next('date_created', is_next=False)
        next_version = self.get_previous_or_next('date_created', is_next=True)
        context['previous_version'] = previous_version
        context['next_version'] = next_version
        context['diff'] = self.get_diff(previous_version, self.get_object())
        return context

    def get_previous_or_next(self, field, is_next=False):
        lookuptype = 'gt' if is_next else 'lt'
        order_by = '' if is_next else '-'
        annotate = {'%s' % field: F('revision__%s' % field)}
        kwargs = {'%s__%s' % (field, lookuptype): getattr(self.get_object().revision, field)}
        logline = Logline.objects.get(id=self.kwargs['logline_pk'])
        qs = Version._default_manager.annotate(**annotate).filter(**kwargs).order_by('%s%s' % (order_by, field)).get_for_object(logline)
        return qs.first()

    def get_diff(self, obj1, obj2):
        if obj1 is not None:
            dmp = PrettyDiffMatchPatch()
            diff = dmp.diff_main(obj1.field_dict['body'], obj2.object.body)
            dmp.diff_cleanupSemantic(diff)
            return dmp.diff_prettyHtml(diff)
        return ''
