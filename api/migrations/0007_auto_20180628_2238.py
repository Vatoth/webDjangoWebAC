# Generated by Django 2.0.6 on 2018-06-28 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180628_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='links',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='userId',
            field=models.IntegerField(default=2),
        ),
    ]
