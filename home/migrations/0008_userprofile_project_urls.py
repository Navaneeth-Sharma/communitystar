# Generated by Django 3.2.10 on 2021-12-11 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='project_urls',
            field=models.JSONField(default=dict),
        ),
    ]
