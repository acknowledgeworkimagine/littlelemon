# Generated by Django 5.0.6 on 2024-05-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_delete_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='inventory',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
