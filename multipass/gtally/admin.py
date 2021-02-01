from django.contrib import admin

# Register your models here.
from .models import Tally, Total

admin.site.register(Tally)
admin.site.register(Total)