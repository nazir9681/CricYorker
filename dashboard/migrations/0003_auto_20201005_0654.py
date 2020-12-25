# Generated by Django 3.1.1 on 2020-10-05 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20201005_0640'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmanage',
            name='package_name',
            field=models.ForeignKey(default='5', on_delete=django.db.models.deletion.CASCADE, related_name='packagename', to='dashboard.packagemanage'),
        ),
        migrations.AlterField(
            model_name='transactionmanage',
            name='user_name',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='username', to='dashboard.user'),
        ),
    ]