# Generated by Django 2.1.5 on 2020-06-17 20:30

from django.db import migrations, models
import zinnia.models_bases.entry


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0002_auto_20200617_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='video_cuantro',
        ),
        migrations.AddField(
            model_name='entry',
            name='video_cuatro',
            field=models.FileField(blank=True, null=True, upload_to=zinnia.models_bases.entry.CoreEntry.get_imagen_video, verbose_name='video_cuatro'),
        ),
    ]
