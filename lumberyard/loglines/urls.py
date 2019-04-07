from django.urls import path

from .views import (
    LoglineCreateView,
    LoglineDetailView,
    LoglineListView,
    LoglineUpdateView,
    VersionDetailView
)


app_name = 'loglines'

urlpatterns = [
    path('new/', LoglineCreateView.as_view(), name='logline_create'),
    path('<int:pk>/update/', LoglineUpdateView.as_view(), name='logline_update'),
    path('<int:logline_pk>/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
    path('<int:pk>/', LoglineDetailView.as_view(), name='logline_detail'),
    path('', LoglineListView.as_view(), name='logline_list'),
]
