# Generated by Django 3.2.15 on 2022-10-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20221026_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='friendly_name',
            field=models.CharField(blank=True, default=False, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]