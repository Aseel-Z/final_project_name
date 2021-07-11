# Generated by Django 3.2.5 on 2021-07-11 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu_hub', '0011_auto_20210711_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='member_1',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='member_2',
        ),
        migrations.AddField(
            model_name='chat',
            name='recipient_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='edu_hub.member'),
        ),
    ]
