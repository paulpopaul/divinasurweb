# Generated by Django 2.1.5 on 2020-06-18 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0003_auto_20200617_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='ruleta_estado',
            field=models.CharField(choices=[('mostrar', 'Mostrar'), ('ocultar', 'Ocultar')], default='ocultar', help_text='Estado', max_length=13, verbose_name='ruleta estado'),
        ),
    ]
