# Generated by Django 2.0.5 on 2018-05-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0005_auto_20180524_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canton',
            name='cars_pp',
        ),
        migrations.RemoveField(
            model_name='city',
            name='cars_pp',
        ),
        migrations.RemoveField(
            model_name='country',
            name='cars_pp',
        ),
        migrations.AddField(
            model_name='canton',
            name='cars',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='cars',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='cars',
            field=models.IntegerField(null=True),
        ),
    ]
