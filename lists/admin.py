from django.contrib import admin

from .models import Entry, List

# Register your models here.

admin.site.register(Entry)
admin.site.register(List)