from django.contrib import admin
from .models import Inv_Item
from .models import Warehouse

# Register your models here.
@admin.register(Inv_Item)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
