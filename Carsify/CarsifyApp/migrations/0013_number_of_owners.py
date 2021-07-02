# Generated by Django 3.2.2 on 2021-07-02 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarsifyApp', '0012_auto_20210630_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number_of_Owners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owners', models.IntegerField(null=True)),
                ('carid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsifyApp.individual_car_details')),
            ],
        ),
    ]
