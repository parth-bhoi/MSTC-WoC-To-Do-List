# Generated by Django 2.1.4 on 2018-12-26 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20181226_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Task_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('due_date', models.DateField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Task_date')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
