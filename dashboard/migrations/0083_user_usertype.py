# Generated by Django 3.1.1 on 2020-10-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0082_auto_20201027_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userType',
            field=models.CharField(choices=[('DEMO', 'DEMO'), ('REAL', 'REAL USER')], default='REAL', max_length=15),
        ),
    ]
