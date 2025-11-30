from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_products, name='products'),             # list of all products
    path('<str:sku>/', views.product_detail, name='product_detail'),  # product detail by SKU
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
