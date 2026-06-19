# products/urls.py
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('<str:sku>/', views.product_detail, name='product_detail'),
    path('<str:sku>/review/add/', views.add_review, name='add_review'),
    path('<str:sku>/review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('<str:sku>/review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('<str:sku>/wishlist/add/', views.add_to_wishlist, name='add_to_wishlist'),
    path('<str:sku>/wishlist/remove/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
