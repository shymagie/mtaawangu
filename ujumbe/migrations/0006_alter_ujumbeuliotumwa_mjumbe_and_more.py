# Generated by Django 4.2.4 on 2023-09-30 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_kata_wilaya_alter_mtaa_kata_and_more'),
        ('ujumbe', '0005_alter_ujumbe_mjumbe_alter_ujumbe_mtendaji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ujumbeuliotumwa',
            name='mjumbe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zilizotumwa_mjumbe', to='users.mjumbe'),
        ),
        migrations.AlterField(
            model_name='ujumbeuliotumwa',
            name='mtendaji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zilizotumwa_mtendaji', to='users.mtendaji'),
        ),
    ]
