from django import forms
from .models import Inv_Item

class PostForm(forms.ModelForm):
    class Meta:
        model = Inv_Item
        fields = "__all__"
