# Generated by Django 3.1.1 on 2020-10-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0069_auto_20201017_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
