# Generated by Django 5.0.4 on 2024-04-06 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=4)),
                ('hip_girth', models.DecimalField(decimal_places=1, max_digits=4)),
                ('biceps_girth', models.DecimalField(decimal_places=1, max_digits=4)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
        ),
    ]
