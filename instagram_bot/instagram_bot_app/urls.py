from django.urls import path

from instagram_bot_app.APIs.instagram_replies import Instagram_hook
from instagram_bot_app.APIs.add_menu import MenuWithOptionsAPIView
from . import views

urlpatterns = [
    path('instagram_webhook/', Instagram_hook.as_view(), name='instagram_webhook'),
    path('add-menu/', MenuWithOptionsAPIView.as_view(), name='menu-with-options-create'),
]

