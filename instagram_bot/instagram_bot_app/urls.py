from django.urls import path
from . import views

urlpatterns = [
    path('instagram_webhook/', views.instagram_webhook, name='instagram_webhook'),
]