# Generated by Django 3.1.1 on 2020-10-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_user_fcm_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmanage',
            name='player_name',
            field=models.CharField(default='Fri Oct  9 10:50:28 2020', max_length=60),
        ),
    ]
