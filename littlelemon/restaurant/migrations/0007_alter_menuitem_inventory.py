# Generated by Django 5.0.6 on 2024-05-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='inventory',
            field=models.IntegerField(default=False),
        ),
    ]
