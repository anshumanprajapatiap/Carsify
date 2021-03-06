# Generated by Django 3.2.2 on 2021-06-11 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarsifyApp', '0009_address_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_Company_Name', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car_Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_Fuel_Type', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_Model_Name', models.TextField(null=True)),
                ('Company_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsifyApp.car_company')),
            ],
        ),
        migrations.CreateModel(
            name='India_States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State_Name', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transmission_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tranmission', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='PanNumber',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='VoterID',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Individual_Car_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_Manufacturing', models.DateField(null=True)),
                ('Card_Registration_Number', models.TextField(null=True)),
                ('Car_Varient', models.TextField(null=True)),
                ('KM', models.IntegerField(null=True)),
                ('Color', models.TextField(null=True)),
                ('Images', models.ImageField(null=True, upload_to='')),
                ('Price', models.IntegerField(null=True)),
                ('Insurance', models.TextField(null=True)),
                ('Insurance_Type', models.TextField(null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsifyApp.car_company')),
                ('Fuel_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsifyApp.car_fuel')),
                ('Model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsifyApp.car_model')),
                ('Registration_State', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsifyApp.india_states')),
                ('Transmission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsifyApp.transmission_type')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
