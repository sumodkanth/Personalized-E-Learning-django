# Generated by Django 5.0.2 on 2024-06-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_custuser_course_alter_custuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=100, null=True),
        ),
    ]