# Generated by Django 3.1.7 on 2021-02-27 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='estimated_time',
            new_name='estimated_date',
        ),
    ]
