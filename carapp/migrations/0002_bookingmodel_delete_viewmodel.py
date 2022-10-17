# Generated by Django 4.1.1 on 2022-10-12 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookingmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('vehiclename', models.CharField(max_length=200, null=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('booking', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='viewmodel',
        ),
    ]