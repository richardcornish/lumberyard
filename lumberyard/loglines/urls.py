from django.urls import path

from .views import (
    LoglineCreateView,
    LoglineDetailView,
    LoglineListView,
    LoglineUpdateView,
    LoglineHistoryDetailView
)


app_name = 'loglines'

urlpatterns = [
    path('new/', LoglineCreateView.as_view(), name='logline_create'),
    path('<int:pk>/history/<int:history_pk>/', LoglineHistoryDetailView.as_view(), name='logline_detail_history'),
    path('<int:pk>/update/', LoglineUpdateView.as_view(), name='logline_update'),
    path('<int:pk>/', LoglineDetailView.as_view(), name='logline_detail'),
    path('', LoglineListView.as_view(), name='logline_list'),
]
