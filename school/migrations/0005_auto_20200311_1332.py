# Generated by Django 3.0.3 on 2020-03-11 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='isshow',
            field=models.BooleanField(default=True, verbose_name='게시여부'),
        ),
        migrations.CreateModel(
            name='Comroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='컴퓨터', max_length=64, verbose_name='교실명')),
                ('caption', models.TextField(null=True, verbose_name='교실설명')),
                ('classNo', models.IntegerField(verbose_name='교실번호')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School', verbose_name='학교')),
            ],
        ),
    ]
