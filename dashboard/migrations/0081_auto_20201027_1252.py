# Generated by Django 3.1.1 on 2020-10-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0080_demouser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demouser',
            name='select_match_demo',
            field=models.ManyToManyField(to='dashboard.PostManage'),
        ),
    ]
