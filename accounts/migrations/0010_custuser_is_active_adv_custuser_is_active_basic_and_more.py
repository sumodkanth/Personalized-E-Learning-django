# Generated by Django 5.0.2 on 2024-02-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='custuser',
            name='is_active_adv',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='custuser',
            name='is_active_basic',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='custuser',
            name='is_active_coding',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='custuser',
            name='is_active_inter',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
