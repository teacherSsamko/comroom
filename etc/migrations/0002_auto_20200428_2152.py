# Generated by Django 3.0.3 on 2020-04-28 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice_nocookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.TextField(verbose_name='공지')),
                ('modified_date', models.DateTimeField(auto_now_add=True, verbose_name='수정날짜')),
            ],
            options={
                'verbose_name': '공지사항',
                'verbose_name_plural': '공지사항',
            },
        ),
        migrations.AlterModelOptions(
            name='disabled_ch',
            options={'verbose_name': '불가 채널', 'verbose_name_plural': '불가 채널'},
        ),
    ]
