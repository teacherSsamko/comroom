# Generated by Django 3.0.3 on 2020-04-29 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0005_auto_20200429_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rollfile',
            name='roll_file',
            field=models.FileField(upload_to='rolls/%Y/'),
        ),
    ]
