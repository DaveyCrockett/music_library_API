# Generated by Django 3.1.8 on 2021-07-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
