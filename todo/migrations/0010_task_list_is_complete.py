# Generated by Django 2.1.4 on 2019-01-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20181227_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_list',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]