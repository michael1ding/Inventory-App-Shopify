# Generated by Django 4.0 on 2022-05-16 05:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2500)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]