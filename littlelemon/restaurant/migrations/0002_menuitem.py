# Generated by Django 5.0.6 on 2024-05-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=6)),
                ('featured', models.BooleanField(db_index=True)),
            ],
        ),
    ]
