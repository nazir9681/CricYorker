# Generated by Django 3.1.1 on 2020-10-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0052_auto_20201015_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanage',
            name='active_post',
            field=models.CharField(default='Thu Oct 15 22:52:52 2020', editable=False, max_length=60),
        ),
        migrations.AlterField(
            model_name='teamcreatepost',
            name='team_imageUpload',
            field=models.ImageField(default='upload/images/pexels-ave-calvar-martinez-4852353_ZZZxG7O.jpg', upload_to='', verbose_name='upload/images/'),
        ),
    ]