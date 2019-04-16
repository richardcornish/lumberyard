from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Logline


admin.site.register(Logline, SimpleHistoryAdmin)
