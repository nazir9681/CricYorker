# Generated by Django 3.1.1 on 2020-10-17 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0063_postmanage_active_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanage',
            name='active_post_time',
            field=models.CharField(default='23:54:20', max_length=60),
        ),
    ]
