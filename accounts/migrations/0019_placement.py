# Generated by Django 5.0.2 on 2024-06-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_custuser_is_hr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
