from django.contrib import admin
from .models import MassNotification, IndividualNotification


@admin.register(MassNotification)
class StatusTestAdmin(admin.ModelAdmin):
    pass


@admin.register(IndividualNotification)
class CategoryAdmin(admin.ModelAdmin):
    pass
