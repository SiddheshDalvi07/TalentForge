# Generated by Django 5.0.4 on 2024-05-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='logo',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]
