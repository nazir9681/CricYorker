# Generated by Django 3.1.1 on 2020-10-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0049_auto_20201015_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(default='Thu Oct 15 22:40:33 2020', editable=False, max_length=60),
        ),
    ]
