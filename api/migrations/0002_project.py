# Generated by Django 2.0.6 on 2018-06-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descriptive', models.TextField()),
                ('userId', models.IntegerField()),
                ('languages', models.ManyToManyField(related_name='_project_languages_+', to='api.Project')),
                ('links', models.ManyToManyField(related_name='_project_links_+', to='api.Project')),
            ],
        ),
    ]
