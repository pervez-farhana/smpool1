# Generated by Django 3.0.5 on 2020-05-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_desc', models.CharField(max_length=500)),
                ('service_cost', models.FloatField()),
            ],
        ),
    ]
