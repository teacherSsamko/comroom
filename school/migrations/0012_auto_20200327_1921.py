# Generated by Django 3.0.3 on 2020-03-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_adminuser_auth_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='auth_key',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='인증키'),
        ),
        migrations.AlterField(
            model_name='adminuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='adminuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='인증여부'),
        ),
    ]