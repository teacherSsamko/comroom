# Generated by Django 3.0.3 on 2020-03-18 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20200317_0308'),
        ('timetable', '0011_fixedtimetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedtimetable',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.School', verbose_name='학교'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fixedtimetable',
            name='comroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.Comroom', verbose_name='교실'),
        ),
    ]