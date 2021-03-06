# Generated by Django 2.2.2 on 2019-06-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_coldwatertable_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricityTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateyear', models.IntegerField(default=2019)),
                ('datemonth', models.PositiveSmallIntegerField(default=6)),
                ('ed_building1_1', models.FloatField(blank=True, null=True)),
                ('ed_building1_2', models.FloatField(blank=True, null=True)),
                ('ed_building1_3', models.FloatField(blank=True, null=True)),
                ('ed_building2_1', models.FloatField(blank=True, null=True)),
                ('ed_building2_2', models.FloatField(blank=True, null=True)),
                ('ed_building2_3', models.FloatField(blank=True, null=True)),
                ('ed_building2_4', models.FloatField(blank=True, null=True)),
                ('ed_building2_5', models.FloatField(blank=True, null=True)),
                ('ed_building2_6', models.FloatField(blank=True, null=True)),
                ('ed_building2a_1', models.FloatField(blank=True, null=True)),
                ('ed_building2a_2', models.FloatField(blank=True, null=True)),
                ('ed_building2a_3', models.FloatField(blank=True, null=True)),
                ('ed_building2a_4', models.FloatField(blank=True, null=True)),
                ('ed_building2a_5', models.FloatField(blank=True, null=True)),
                ('ed_building2a_6', models.FloatField(blank=True, null=True)),
                ('ed_building6_1', models.FloatField(blank=True, null=True)),
                ('ed_building6_2', models.FloatField(blank=True, null=True)),
                ('ed_building6_3', models.FloatField(blank=True, null=True)),
                ('ed_building6_4', models.FloatField(blank=True, null=True)),
                ('ed_building7_1', models.FloatField(blank=True, null=True)),
                ('ed_building7_2', models.FloatField(blank=True, null=True)),
                ('barn', models.FloatField(blank=True, null=True)),
                ('canteen', models.FloatField(blank=True, null=True)),
                ('garage_1', models.FloatField(blank=True, null=True)),
                ('garage_2', models.FloatField(blank=True, null=True)),
                ('garage_3', models.FloatField(blank=True, null=True)),
                ('proving_ground', models.FloatField(blank=True, null=True)),
                ('pavilion', models.FloatField(blank=True, null=True)),
                ('hostel1', models.FloatField(blank=True, null=True)),
                ('hostel2', models.FloatField(blank=True, null=True)),
                ('hostel3', models.FloatField(blank=True, null=True)),
                ('hostel4', models.FloatField(blank=True, null=True)),
                ('hostel5', models.FloatField(blank=True, null=True)),
                ('hostel6_1', models.FloatField(blank=True, null=True)),
                ('hostel6_2', models.FloatField(blank=True, null=True)),
                ('hostel7_1', models.FloatField(blank=True, null=True)),
                ('hostel7_2', models.FloatField(blank=True, null=True)),
                ('hostel8_1', models.FloatField(blank=True, null=True)),
                ('hostel8_2', models.FloatField(blank=True, null=True)),
                ('hostel8_3', models.FloatField(blank=True, null=True)),
                ('TP38_1', models.FloatField(blank=True, null=True)),
                ('TP38_2', models.FloatField(blank=True, null=True)),
                ('TP38_3', models.FloatField(blank=True, null=True)),
                ('TP72_1', models.FloatField(blank=True, null=True)),
                ('TP72_2', models.FloatField(blank=True, null=True)),
                ('TP72_3', models.FloatField(blank=True, null=True)),
                ('institute', models.FloatField(blank=True, null=True)),
                ('date', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HotWaterTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateyear', models.IntegerField(default=2019)),
                ('datemonth', models.PositiveSmallIntegerField(default=6)),
                ('hostel7_1', models.FloatField(blank=True, null=True)),
                ('hostel7_2', models.FloatField(blank=True, null=True)),
                ('hostel8_1', models.FloatField(blank=True, null=True)),
                ('hostel8_2', models.FloatField(blank=True, null=True)),
                ('date', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateyear', models.IntegerField(default=2019)),
                ('datemonth', models.PositiveSmallIntegerField(default=6)),
                ('ed_building1', models.FloatField(blank=True, null=True)),
                ('ed_building2', models.FloatField(blank=True, null=True)),
                ('ed_building4', models.FloatField(blank=True, null=True)),
                ('ed_building5', models.FloatField(blank=True, null=True)),
                ('ed_building6', models.FloatField(blank=True, null=True)),
                ('ed_building7', models.FloatField(blank=True, null=True)),
                ('garage', models.FloatField(blank=True, null=True)),
                ('sport_building', models.FloatField(blank=True, null=True)),
                ('canteen', models.FloatField(blank=True, null=True)),
                ('hostel1', models.FloatField(blank=True, null=True)),
                ('hostel2', models.FloatField(blank=True, null=True)),
                ('hostel3', models.FloatField(blank=True, null=True)),
                ('hostel4', models.FloatField(blank=True, null=True)),
                ('hostel5', models.FloatField(blank=True, null=True)),
                ('hostel6', models.FloatField(blank=True, null=True)),
                ('hostel7', models.FloatField(blank=True, null=True)),
                ('hostel8', models.FloatField(blank=True, null=True)),
                ('pavilion', models.FloatField(blank=True, null=True)),
                ('car_fleet', models.FloatField(blank=True, null=True)),
                ('boiler_house', models.FloatField(blank=True, null=True)),
                ('institute', models.FloatField(blank=True, null=True)),
                ('date', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WarmTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateyear', models.IntegerField(default=2019)),
                ('datemonth', models.PositiveSmallIntegerField(default=6)),
                ('ed_building1', models.FloatField(blank=True, null=True)),
                ('hostel7', models.FloatField(blank=True, null=True)),
                ('hostel8', models.FloatField(blank=True, null=True)),
                ('boiler_house', models.FloatField(blank=True, null=True)),
                ('institute', models.FloatField(blank=True, null=True)),
                ('date', models.IntegerField(default=0)),
            ],
        ),
    ]
