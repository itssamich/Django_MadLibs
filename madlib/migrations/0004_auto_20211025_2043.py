# Generated by Django 2.2 on 2021-10-26 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madlib', '0003_auto_20211025_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='madlib',
            name='story',
        ),
        migrations.AddField(
            model_name='madlib',
            name='part1',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='madlib',
            name='part2',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='madlib',
            name='part3',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='madlib',
            name='part4',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='madlib',
            name='part5',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='madlib',
            name='part6',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='madlib',
            name='part7',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='madlib',
            name='part8',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
