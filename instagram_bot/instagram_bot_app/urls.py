from django.urls import path

from instagram_bot_app.APIs.add_menu import MenuWithOptionsAPIView
from . import views

urlpatterns = [
    path('instagram_webhook/', views.instagram_webhook, name='instagram_webhook'),
    path('add-menu/', MenuWithOptionsAPIView.as_view(), name='menu-with-options-create'),
]