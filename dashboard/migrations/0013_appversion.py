# Generated by Django 3.1.1 on 2020-10-09 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_delete_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('version', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
