# Generated by Django 3.1.1 on 2020-10-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20201009_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appversion',
            name='url',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]