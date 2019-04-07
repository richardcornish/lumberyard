from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView, TemplateView


class FaviconView(RedirectView):
    url = staticfiles_storage.url('img/favicon.ico')
    permanent = False


class HomeView(TemplateView):
    template_name = 'home.html'


class NotFoundView(TemplateView):
    template_name = '404.html'


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
