# Generated by Django 3.1.1 on 2021-01-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('problem', models.CharField(max_length=22)),
                ('place', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('appno', models.IntegerField()),
                ('doctor', models.CharField(max_length=60)),
            ],
        ),
    ]
