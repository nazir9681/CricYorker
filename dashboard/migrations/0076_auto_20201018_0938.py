# Generated by Django 3.1.1 on 2020-10-18 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0075_auto_20201018_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagemanage',
            name='discount_price',
            field=models.IntegerField(verbose_name='Discount Percentage'),
        ),
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(default='18 Oct 2020 09:38:17', max_length=60),
        ),
    ]