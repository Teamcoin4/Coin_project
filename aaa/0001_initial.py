# Generated by Django 5.1.7 on 2025-03-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('user_pw', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
    ]
