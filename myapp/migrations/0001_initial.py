# Generated by Django 3.2 on 2021-05-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=255)),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
    ]