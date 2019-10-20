from django.urls import path
from . import views

urlpatterns = [
    path('currencies/', views.currencies),
    path('rate/<int:currency_id>', views.rate),
    path('rate/refresh', views.refresh),
]
