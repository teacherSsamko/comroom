# Generated by Django 3.0.3 on 2020-03-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20200319_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='인증여부'),
        ),
    ]
