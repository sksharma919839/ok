# Generated by Django 5.1 on 2024-09-30 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hservice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='image/')),
                ('upload_to', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(max_length=555)),
                ('deatail', models.CharField(max_length=999)),
                ('link', models.CharField(max_length=999)),
            ],
        ),
    ]
