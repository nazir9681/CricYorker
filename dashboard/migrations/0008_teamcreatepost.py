# Generated by Django 3.1.1 on 2020-10-06 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20201005_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamCreatePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_imageUpload', models.ImageField(blank=True, null=True, upload_to='', verbose_name='upload/images/')),
                ('status', models.CharField(choices=[('1', 'ACTIVE'), ('0', 'INACIVE')], default='1', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postmanage', to='dashboard.postmanage')),
            ],
            options={
                'verbose_name_plural': 'Team Create',
            },
        ),
    ]