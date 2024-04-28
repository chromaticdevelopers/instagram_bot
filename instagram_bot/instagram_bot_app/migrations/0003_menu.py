# Generated by Django 5.0.4 on 2024-04-28 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_bot_app', '0002_userstatus_last_login_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('main_menu', models.BooleanField(default=False)),
            ],
        ),
    ]
