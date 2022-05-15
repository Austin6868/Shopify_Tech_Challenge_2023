from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Inv_Item
from .models import Warehouse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


# Create your views here.
class IndexView(ListView):
    model = Inv_Item
    template_name = 'Logi_App/index.html'
    context_object_name = 'post_list'

class SingleView(DetailView):
    model = Inv_Item
    template_name = 'Logi_App/single.html'
    context_object_name = 'post'

class PostView(ListView):
    model = Inv_Item
    template_name = "Logi_App/posts.html"
    context_object_name = 'post_list'

class AddView(CreateView):
    model = Inv_Item
    template_name = 'Logi_App/add.html'
    fields = '__all__'
    success_url = reverse_lazy('Logi_App:posts')

class EditView(UpdateView):
    model = Inv_Item
    template_name = 'Logi_App/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('Logi_App:posts')

class Delete(DeleteView):
    model = Inv_Item
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('Logi_App:posts')
    template_name = 'Logi_App/confirm-delete.html'
