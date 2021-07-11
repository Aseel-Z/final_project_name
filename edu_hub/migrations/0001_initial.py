# Generated by Django 3.2.5 on 2021-07-10 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.BooleanField(default='False')),
                ('city', models.CharField(choices=[('AMMAN', 'Amman'), ('ZARQA', 'Zarqa'), ('IRBID', 'Irbid'), ('MAFRAQ', 'Mafraq'), ('SALT', 'Salt'), ('MADABA', 'Madaba'), ('AQABA', 'Aqaba'), ('MA`AN', 'Ma`an'), ('JARASH', 'Jarash'), ('AJLUN', 'Ajlun'), ('KARAK', 'Karak'), ('TAFILAH', 'Tafilah')], default='NULL', max_length=255)),
                ('member', models.CharField(choices=[('EDUCATOR', 'educator'), ('ORGANIZATION', 'organization'), ('STUDENT', 'student')], default='NULL', max_length=255)),
                ('first_name', models.CharField(default='NULL', max_length=255)),
                ('last_name', models.CharField(default='NULL', max_length=255)),
                ('organization_name', models.CharField(default='NULL', max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='NULL', max_length=1)),
                ('birth_date', models.DateTimeField(default='NULL')),
                ('password', models.CharField(default='NULL', max_length=255)),
                ('email', models.EmailField(default='NULL', max_length=254)),
                ('mobile_number', models.IntegerField(default='NULL')),
                ('specialization', models.CharField(default='NULL', max_length=255)),
                ('interests', models.TextField(default='NULL')),
                ('biography', models.TextField(default='NULL')),
                ('current_organization', models.CharField(default='NULL', max_length=255)),
                ('organization_summary', models.TextField(default='NULL')),
                ('freelancer', models.BooleanField(default='NULL')),
                ('hourly_tutoring_rate', models.IntegerField(default='NULL')),
                ('services', models.TextField(default='NULL')),
                ('created_at', models.DateTimeField(default='NULL')),
                ('updated_at', models.DateTimeField(default='NULL')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField()),
                ('message_body', models.TextField()),
                ('creator_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='edu_hub.member')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField()),
                ('post_body', models.TextField()),
                ('creator_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='edu_hub.member')),
            ],
        ),
        migrations.CreateModel(
            name='MessageRecipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='edu_hub.message')),
                ('recipient_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='edu_hub.member')),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_date', models.DateTimeField()),
                ('connection_member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connection_member_id', to='edu_hub.member')),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_id', to='edu_hub.member')),
            ],
        ),
    ]