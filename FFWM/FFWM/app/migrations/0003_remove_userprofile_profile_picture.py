# Generated by Django 4.1.4 on 2022-12-23 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userprofile_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
    ]
