# Generated by Django 3.1.1 on 2020-10-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0071_auto_20201018_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]