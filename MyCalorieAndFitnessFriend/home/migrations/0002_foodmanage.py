# Generated by Django 3.2.9 on 2022-06-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('eat', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
            ],
        ),
    ]
