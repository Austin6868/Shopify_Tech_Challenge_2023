from django import forms
from .models import Inv_Item, Warehouse

class PostForm(forms.ModelForm):
    class Meta:
        model = Inv_Item
        fields = "__all__"

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"
