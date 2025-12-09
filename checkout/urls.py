from django.urls import path
from . import views

app_name = 'checkout'  # ← this is required for namespacing

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>/', views.checkout_success, name='checkout_success'),
    path('checkout_failure/', views.checkout_failure, name='checkout_failure'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
]
