# Generated by Django 5.0.4 on 2024-04-28 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_bot_app', '0006_remove_menu_successors_menu_successor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='successor',
            new_name='preceder_of',
        ),
    ]