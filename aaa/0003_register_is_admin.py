# Generated by Django 5.1.7 on 2025-03-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_user_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
