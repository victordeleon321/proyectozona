# Generated by Django 2.1.3 on 2018-11-07 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaje',
            name='imagen',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
