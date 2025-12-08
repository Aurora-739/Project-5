from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<str:order_number>/', views.order_history, name='order_history'),
    path('newsletter/', views.newsletter_signup, name='newsletter_signup'),


]
