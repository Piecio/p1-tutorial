# Generated by Django 2.0 on 2017-12-27 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
    ]