# Generated by Django 4.2 on 2023-05-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
