# Generated by Django 3.2.15 on 2023-02-15 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desserts', '0012_auto_20230215_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linked_recipes',
            name='recipe',
        ),
        migrations.AddField(
            model_name='linked_recipes',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='desserts.recipe'),
        ),
    ]
