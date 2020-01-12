# Generated by Django 3.0.2 on 2020-01-11 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('source', models.TextField()),
                ('prep_time', models.IntegerField()),
                ('cook_time', models.IntegerField()),
                ('servings', models.IntegerField()),
                ('calories', models.FloatField()),
                ('fat', models.FloatField()),
                ('satfat', models.FloatField()),
                ('carbs', models.FloatField()),
                ('fiber', models.FloatField()),
                ('sugar', models.FloatField()),
                ('protein', models.FloatField()),
                ('instructions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('quantity', models.FloatField(default=0)),
                ('unit', models.CharField(max_length=2048)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='ar.Recipe')),
            ],
        ),
    ]