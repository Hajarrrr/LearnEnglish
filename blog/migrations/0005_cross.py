# Generated by Django 3.0.8 on 2020-08-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_verbs'),
    ]

    operations = [
        migrations.CreateModel(
            name='cross',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('eng', models.CharField(max_length=100)),
            ],
        ),
    ]