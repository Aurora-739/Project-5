# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<str:sku>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<str:sku>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<str:sku>/', views.remove_from_bag, name='remove_from_bag'),
    path('bag/update/<str:sku>/', views.update_bag, name='update_bag'),

]
