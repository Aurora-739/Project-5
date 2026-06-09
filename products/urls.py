from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<str:sku>/', views.product_detail, name='product_detail'),
    path('<str:sku>/review/add/', views.add_review, name='add_review'),
    path('<str:sku>/review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('<str:sku>/review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]