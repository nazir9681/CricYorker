# Generated by Django 3.1.1 on 2020-10-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_auto_20201012_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionmanage',
            name='user_orders_id',
        ),
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(default='Mon Oct 12 07:21:10 2020', max_length=60),
        ),
    ]
