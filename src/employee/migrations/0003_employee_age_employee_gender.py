# Generated by Django 4.1.7 on 2023-03-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20200904_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=34, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=34, max_length=30),
            preserve_default=False,
        ),
    ]
