from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('', views.all_products, name='products'),             # list of all products
    path('', views.all_products, name='all_products'),
    path('<str:sku>/', views.product_detail, name='product_detail'),  # product detail by SKU
    path('<int:product_id>/', views.product_detail, name='product_detail'), #product detail
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
