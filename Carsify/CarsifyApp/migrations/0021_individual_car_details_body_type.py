# Generated by Django 3.2.2 on 2021-07-02 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarsifyApp', '0020_car_body_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual_car_details',
            name='Body_Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsifyApp.car_body_type'),
        ),
    ]