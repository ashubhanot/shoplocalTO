# Generated by Django 4.0.1 on 2022-02-21 15:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0012_business_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
