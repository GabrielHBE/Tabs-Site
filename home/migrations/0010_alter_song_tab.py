# Generated by Django 5.1.4 on 2024-12-22 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_instrument_song_instrument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='tab',
            field=models.FileField(blank=True, null=True, upload_to='Tabs/'),
        ),
    ]