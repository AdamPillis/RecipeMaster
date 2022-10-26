# Generated by Django 3.2.15 on 2022-10-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_ingredient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='price',
            new_name='cost_per_quantity_type',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='friendly_name',
            field=models.CharField(default=False, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.SlugField(unique=True),
        ),
    ]
