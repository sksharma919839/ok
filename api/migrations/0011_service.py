# Generated by Django 5.1 on 2024-09-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_vehiclefourth'),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='image/')),
                ('upload_to', models.DateTimeField(auto_now_add=True)),
                ('h5', models.CharField(max_length=455)),
                ('p', models.CharField(max_length=999)),
                ('link', models.CharField(max_length=999)),
            ],
        ),
    ]
