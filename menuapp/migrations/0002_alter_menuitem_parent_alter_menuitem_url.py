# Generated by Django 4.2.6 on 2023-10-06 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menuapp.menuitem'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
