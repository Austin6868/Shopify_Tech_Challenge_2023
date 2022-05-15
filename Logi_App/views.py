from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Inv_Item
from .models import Warehouse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


# Create your views here.
class IndexView(ListView):
    model = Inv_Item
    template_name = 'Logi_App/../templates/index.html'
    context_object_name = 'post_list'

class SingleView(DetailView):
    model = Inv_Item
    template_name = 'Logi_App/../templates/single.html'
    context_object_name = 'post'

class PostView(ListView):
    model = Inv_Item
    template_name = "Logi_App/../templates/posts.html"
    context_object_name = 'post_list'

class AddView(CreateView):
    model = Inv_Item
    template_name = 'Logi_App/../templates/add.html'
    fields = '__all__'
    success_url = reverse_lazy('Logi_App:posts')

class EditView(UpdateView):
    model = Inv_Item
    template_name = 'Logi_App/../templates/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('Logi_App:posts')

class Delete(DeleteView):
    model = Inv_Item
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('Logi_App:posts')
    template_name = 'Logi_App/../templates/confirm-delete.html'

class AddWarehouse(CreateView):
    model = Warehouse
    template_name = 'Logi_App/../templates/add_warehouse.html'
    fields = '__all__'
    success_url = reverse_lazy('Logi_App:posts_warehouse')

class DeleteWarehouse(DeleteView):
    model = Warehouse
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('Logi_App:posts_warehouse')
    template_name = 'Logi_App/../templates/confirm-delete.html'

class PostWarehouse(ListView):
    model = Warehouse
    template_name = "Logi_App/../templates/posts_warehouse.html"
    context_object_name = 'post_list'

