# Generated by Django 4.2.4 on 2023-09-23 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mkoa',
            name='nchi',
            field=models.ForeignKey(default='Tanzania', on_delete=django.db.models.deletion.CASCADE, to='users.nchi'),
        ),
    ]
