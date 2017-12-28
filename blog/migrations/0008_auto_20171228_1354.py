# Generated by Django 2.0 on 2017-12-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171227_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='A short label, generally used in URLs.', max_length=80, unique=True),
        ),
    ]