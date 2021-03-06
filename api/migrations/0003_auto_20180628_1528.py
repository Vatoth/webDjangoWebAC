# Generated by Django 2.0.6 on 2018-06-28 15:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myList', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('note', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='project',
            name='links',
        ),
        migrations.AlterField(
            model_name='project',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='salaryClaims',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='skill',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
