# Generated by Django 3.2.10 on 2021-12-11 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social_django', '0012_delete_userprofile'),
        ('home', '0004_delete_usersocialauth'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSocialAuth',
            fields=[
                ('usersocialauth_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='social_django.usersocialauth')),
                ('profile_url', models.URLField(blank=True)),
                ('avatar_url', models.URLField(blank=True)),
                ('screen_name', models.CharField(blank=True, default='', max_length=200)),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'User Social Auth',
                'verbose_name_plural': 'User Social Auths',
            },
            bases=('social_django.usersocialauth',),
        ),
    ]
