# Generated by Django 3.2.10 on 2021-12-13 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_django', '0012_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectsdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=200)),
                ('creator', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('stage', models.CharField(max_length=100)),
                ('prog', models.CharField(max_length=100)),
                ('org', models.CharField(max_length=1)),
                ('count', models.IntegerField()),
                ('framework', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='projectsTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('project', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Project Taken',
                'verbose_name_plural': 'Projects Taken',
            },
        ),
        migrations.CreateModel(
            name='UserSocialAuth',
            fields=[
                ('usersocialauth_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='social_django.usersocialauth')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'User Social Auth',
                'verbose_name_plural': 'User Social Auths',
            },
            bases=('social_django.usersocialauth',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('project_urls', jsonfield.fields.JSONField(default=dict)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
