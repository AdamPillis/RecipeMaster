# Generated by Django 3.2.15 on 2022-11-03 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('unit', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('quantity_type', models.CharField(choices=[('g', 'g'), ('ml', 'ml')], default=False, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('prep_time', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('cooking_time', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('tools_required', models.TextField()),
                ('step_guide', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='desserts.category')),
                ('ingredients', models.ManyToManyField(to='desserts.Ingredient')),
            ],
        ),
    ]
