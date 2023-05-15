from django.contrib import admin
from .models import City, County
# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'name')