from django.contrib import admin
from .models import ElectroCar, Person

# Register your models here.

admin.site.register(ElectroCar)
admin.site.register(Person)