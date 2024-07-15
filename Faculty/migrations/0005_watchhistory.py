# Generated by Django 5.0.2 on 2024-07-05 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0004_video_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched_at', models.DateTimeField(auto_now_add=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Faculty.video')),
            ],
        ),
    ]
