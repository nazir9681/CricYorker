# Generated by Django 3.1.1 on 2020-10-12 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20201012_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionmanage',
            name='orders_id',
        ),
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(default='Mon Oct 12 06:59:22 2020', max_length=60),
        ),
    ]
