from django.contrib import admin
from .models import Car
from .models import Deal

# Register your models here.
admin.site.register(Car)
admin.site.register(Deal)