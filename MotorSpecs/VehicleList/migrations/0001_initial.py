# Generated by Django 2.1.1 on 2018-10-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carID', models.CharField(max_length=10)),
                ('carMakeName', models.CharField(max_length=50)),
                ('carModel', models.CharField(max_length=50)),
                ('carSeries', models.CharField(max_length=50)),
                ('carSeriesYear', models.CharField(max_length=10)),
                ('carPriceNew', models.CharField(max_length=15)),
                ('carEngineSize', models.CharField(max_length=10)),
                ('carFuelSystem', models.CharField(max_length=50)),
                ('carTankCapacity', models.CharField(max_length=10)),
                ('carPower', models.CharField(max_length=10)),
                ('carSeatingCapacity', models.CharField(max_length=5)),
                ('carStandardTransmission', models.CharField(max_length=10)),
                ('carBodyType', models.CharField(max_length=50)),
                ('carDrive', models.CharField(max_length=10)),
                ('carWheelbase', models.CharField(max_length=10)),
            ],
        ),
    ]