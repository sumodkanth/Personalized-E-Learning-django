# Generated by Django 5.0.2 on 2024-07-14 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0007_watchhistory_course_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchhistory',
            old_name='course_name',
            new_name='course_id',
        ),
    ]