# Generated by Django 5.0.3 on 2024-03-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmease_app', '0013_orderfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderfeedback',
            name='crop_names',
            field=models.TextField(blank=True, null=True),
        ),
    ]
