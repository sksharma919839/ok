# Generated by Django 5.1 on 2024-09-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_vehiclethird'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicleFourth',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='image/')),
                ('upload_to', models.DateTimeField(auto_now_add=True)),
                ('p', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=555)),
            ],
        ),
    ]
