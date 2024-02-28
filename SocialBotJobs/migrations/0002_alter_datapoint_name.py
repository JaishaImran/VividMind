# Generated by Django 4.2.7 on 2023-12-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBotJobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='name',
            field=models.CharField(blank=True, choices=[('from_google_sheet', 'From Google Sheet'), ('with_google_sheet', 'With Google Sheet'), ('login', 'Login')], max_length=100, null=True),
        ),
    ]