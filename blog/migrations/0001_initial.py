# Generated by Django 3.0.8 on 2020-07-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nouns',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('eng', models.CharField(max_length=100)),
                ('fr', models.CharField(max_length=100)),
            ],
        ),
    ]