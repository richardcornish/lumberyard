from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView, TemplateView

from loglines.models import Logline


class FaviconView(RedirectView):
    url = staticfiles_storage.url('img/favicon.ico')
    permanent = False


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logline_list'] = Logline.objects.all()
        return context


class NotFoundView(TemplateView):
    template_name = '404.html'


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
