# Generated by Django 5.0.2 on 2024-06-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_placement_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='placement',
            name='job_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='placement',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
