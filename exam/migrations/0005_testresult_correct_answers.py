# Generated by Django 5.0.2 on 2024-03-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_testresult_is_active_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='correct_answers',
            field=models.JSONField(default=list),
        ),
    ]
