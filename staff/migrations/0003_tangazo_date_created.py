# Generated by Django 4.2.4 on 2023-10-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_ujumbewatangazo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tangazo',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
