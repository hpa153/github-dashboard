# Generated by Django 4.0.6 on 2022-07-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to='account_images/'),
        ),
    ]
