# Generated by Django 3.1.1 on 2020-10-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0038_auto_20201012_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(default='Mon Oct 12 07:42:09 2020', editable=False, max_length=60),
        ),
    ]
