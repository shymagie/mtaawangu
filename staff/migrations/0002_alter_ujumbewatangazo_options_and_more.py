# Generated by Django 4.2.4 on 2023-10-07 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ujumbewatangazo',
            options={'verbose_name_plural': 'JumbeZaMatangazo'},
        ),
        migrations.AlterModelOptions(
            name='ujumbewatangazouliofika',
            options={'verbose_name_plural': 'JumbeZaTangazoZilizoFika'},
        ),
        migrations.AddField(
            model_name='tangazo',
            name='ujumbe',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tangazo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ujumbe_wa_tangazo_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ujumbewatangazo',
            name='ujumbe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.tangazo'),
        ),
    ]
