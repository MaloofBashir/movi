from django.contrib import admin

# Register your models here.

from .models import Registration,Movie

admin.site.register(Registration)
admin.site.register(Movie)