from django.urls import path
from . import views

app_name = 'Logi_App'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add', views.AddView.as_view(), name='add'),
    path('add_warehouse', views.AddWarehouse.as_view(), name='add_warehouse'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path('posts_warehouse/', views.PostWarehouse.as_view(), name='posts_warehouse'),
    path('<slug:slug>/', views.SingleView.as_view(), name='single'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('delete_warehouse/<int:pk>/', views.DeleteWarehouse.as_view(), name='confirm-delete_warehouse'),
]
