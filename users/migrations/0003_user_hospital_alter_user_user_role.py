# Generated by Django 5.1.1 on 2024-10-26 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
        ('users', '0002_alter_user_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(blank=True, choices=[('admin', 'NurseAdmin'), ('nurse', 'Nurse'), ('chp', 'Community Health Promoter')], max_length=50, null=True),
        ),
    ]
