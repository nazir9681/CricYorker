# Generated by Django 3.1.1 on 2020-10-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_auto_20201012_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmanage',
            name='user_orders_id',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(default='Mon Oct 12 07:23:38 2020', max_length=60),
        ),
    ]
