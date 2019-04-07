from django.contrib import admin

from reversion.admin import VersionAdmin

from .models import Logline


@admin.register(Logline)
class LoglineAdmin(VersionAdmin):
    pass
