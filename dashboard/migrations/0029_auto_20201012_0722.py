# Generated by Django 3.1.1 on 2020-10-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_auto_20201012_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(default='Mon Oct 12 07:22:34 2020', max_length=60),
        ),
    ]
