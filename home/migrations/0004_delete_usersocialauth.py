# Generated by Django 3.2.10 on 2021-12-11 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_usersocialauth_screen_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserSocialAuth',
        ),
    ]
