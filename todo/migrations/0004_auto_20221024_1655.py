# Generated by Django 3.2 on 2022-10-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todolist_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
