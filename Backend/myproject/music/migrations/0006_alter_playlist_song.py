# Generated by Django 5.2 on 2025-05-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_alter_customuser_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(blank=True, to='music.track'),
        ),
    ]
