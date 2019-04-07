from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import HomeView


urlpatterns = [
    path('loglines/', include('loglines.urls')),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', HomeView.as_view(), name='home'),
]


if getattr(settings, 'DEBUG', False):
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
