# Generated by Django 5.0.6 on 2024-07-01 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0013_alter_shopping_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping',
            name='amount',
        ),
    ]
