# Generated by Django 5.0.2 on 2024-07-14 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0009_alter_watchhistory_course_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchhistory',
            old_name='video',
            new_name='video_id',
        ),
    ]
