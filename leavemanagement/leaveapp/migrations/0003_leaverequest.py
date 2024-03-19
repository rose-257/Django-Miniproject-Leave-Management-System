# Generated by Django 5.0.1 on 2024-02-08 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0002_delete_leaverequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='leaverequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('days', models.IntegerField()),
                ('reason', models.CharField(max_length=200, null=True)),
                ('leaveapprovalstatus', models.BooleanField(default=False)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='leaveapp.student')),
            ],
        ),
    ]
