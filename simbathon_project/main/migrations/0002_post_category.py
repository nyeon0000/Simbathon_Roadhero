# Generated by Django 4.0.5 on 2022-07-02 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
