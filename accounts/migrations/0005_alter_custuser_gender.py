# Generated by Django 4.2.7 on 2023-12-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_custuser_age_custuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=100, null=True),
        ),
    ]
