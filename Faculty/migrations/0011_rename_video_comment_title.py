# Generated by Django 5.0.2 on 2024-07-16 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0010_rename_video_watchhistory_video_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='video',
            new_name='title',
        ),
    ]