# Generated by Django 3.2.2 on 2021-07-02 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarsifyApp', '0019_individual_car_details_owners'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Body_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_type', models.TextField(null=True)),
            ],
        ),
    ]
