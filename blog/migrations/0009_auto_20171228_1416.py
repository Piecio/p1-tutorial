# Generated by Django 2.0 on 2017-12-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171228_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='A short label, generally used in URLs.', max_length=80, unique_for_date='publish'),
        ),
    ]
