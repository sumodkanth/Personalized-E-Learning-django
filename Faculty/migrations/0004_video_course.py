# Generated by Django 5.0.2 on 2024-04-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0003_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]