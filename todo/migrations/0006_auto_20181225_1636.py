# Generated by Django 2.1.4 on 2018-12-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_task_is_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(),
        ),
    ]