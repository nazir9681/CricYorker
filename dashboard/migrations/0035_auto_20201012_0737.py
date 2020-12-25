# Generated by Django 3.1.1 on 2020-10-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0034_auto_20201012_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(default='Mon Oct 12 07:37:12 2020', editable=False, max_length=60),
        ),
        migrations.AlterField(
            model_name='transactionmanage',
            name='paid_status',
            field=models.CharField(choices=[('1', 'ACTIVE'), ('0', 'INACIVE')], default='0', editable=False, max_length=1),
        ),
    ]
