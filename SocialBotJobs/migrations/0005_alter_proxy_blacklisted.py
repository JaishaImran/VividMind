# Generated by Django 4.2.7 on 2023-12-30 13:03

import SocialBotJobs.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBotJobs', '0004_alter_proxy_blacklisted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxy',
            name='blacklisted',
            field=SocialBotJobs.models.UppercaseBooleanField(default=False),
        ),
    ]
