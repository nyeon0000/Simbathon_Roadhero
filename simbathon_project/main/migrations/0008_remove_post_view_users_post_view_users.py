# Generated by Django 4.0.5 on 2022-07-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_post_view_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='view_users',
        ),
        migrations.AddField(
            model_name='post',
            name='view_users',
            field=models.IntegerField(default=0),
        ),
    ]
