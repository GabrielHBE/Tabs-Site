# Generated by Django 5.1.4 on 2024-12-20 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='Audios/'),
        ),
        migrations.AddField(
            model_name='song',
            name='yt_video',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='tab',
            field=models.FileField(blank=True, upload_to='Tab_files/'),
        ),
    ]
