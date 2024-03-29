# Generated by Django 4.2.7 on 2024-01-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBotJobs', '0005_alter_proxy_blacklisted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_id', models.CharField(max_length=255, unique=True)),
                ('server_name', models.CharField(max_length=255)),
                ('load', models.FloatField()),
                ('last_beat', models.DateTimeField()),
                ('tags', models.CharField(max_length=255)),
            ],
        ),
    ]
