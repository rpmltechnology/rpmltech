# Generated by Django 2.2.3 on 2021-02-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acheivement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_no_of_client', models.IntegerField()),
                ('Trusted', models.IntegerField()),
                ('Locations', models.IntegerField()),
                ('Consulting_services', models.IntegerField()),
            ],
        ),
    ]