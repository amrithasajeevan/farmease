# Generated by Django 5.0.1 on 2024-03-01 05:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmease_app', '0003_remove_farmerproduct_is_available_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgricultureOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FarmOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('crop_names', models.TextField(blank=True, null=True)),
                ('quantities', models.TextField(blank=True, null=True)),
                ('prices', models.TextField(blank=True, null=True)),
                ('total', models.FloatField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('estimated_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('order-placed', 'order-placed'), ('cancelled', 'cancelled')], default='order-placed', max_length=200)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
