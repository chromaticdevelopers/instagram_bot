from rest_framework import serializers
from .models import Menu, OptionsMenu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'subtitle', 'image_url', 'main_menu', 'successor_of']

class OptionsMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsMenu
        fields = ['menu', 'title', 'type']
