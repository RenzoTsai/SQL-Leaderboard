# Generated by Django 4.0.3 on 2022-03-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='querytask',
            name='query_type',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public')], max_length=32, null=True),
        ),
    ]
