# Generated by Django 2.1.1 on 2018-10-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeID', models.CharField(max_length=250)),
                ('storeName', models.CharField(max_length=250)),
                ('storeAddress', models.CharField(max_length=75)),
                ('storePhone', models.CharField(max_length=50)),
                ('storeCity', models.CharField(max_length=75)),
                ('storeStateName', models.CharField(max_length=75)),
            ],
        ),
    ]
