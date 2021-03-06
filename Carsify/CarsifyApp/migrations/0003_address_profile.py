# Generated by Django 3.2.2 on 2021-06-11 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarsifyApp', '0002_auto_20210611_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100, null=True)),
                ('apartment_address', models.CharField(max_length=100, null=True)),
                ('country', models.TextField(max_length=100, null=True)),
                ('zip', models.CharField(max_length=100, null=True)),
                ('usr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProfileImg', models.FileField(null=True, upload_to='')),
                ('ContactNo', models.IntegerField(null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('AddharNumber', models.IntegerField(null=True)),
                ('PanNumber', models.IntegerField(null=True)),
                ('VoterID', models.IntegerField(null=True)),
                ('Address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsifyApp.address')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
