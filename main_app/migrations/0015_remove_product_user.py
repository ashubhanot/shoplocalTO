# Generated by Django 4.0.1 on 2022-02-22 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]