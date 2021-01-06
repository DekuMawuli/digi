# Generated by Django 3.1.5 on 2021-01-06 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_open', models.BooleanField(default=True)),
                ('call_number', models.CharField(default='', max_length=25)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='BranchBuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('departure_time', models.TimeField()),
                ('is_full', models.BooleanField(default=False)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='booker.branch')),
            ],
            options={
                'verbose_name_plural': 'Branch Buses',
            },
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(default=0)),
                ('number_plate', models.CharField(max_length=10)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'On Road'), (2, 'Available'), (3, 'Faulty')], default=2)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ManyToManyField(through='booker.BranchBuses', to='booker.Branch')),
            ],
            options={
                'verbose_name_plural': 'Buses',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('license_code', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusSeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(default='', max_length=100)),
                ('passenger_phone', models.CharField(default='', max_length=10)),
                ('is_booked', models.BooleanField(default=False)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booker.bus')),
            ],
            options={
                'verbose_name_plural': 'Bus Seats',
            },
        ),
        migrations.AddField(
            model_name='bus',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booker.driver'),
        ),
        migrations.AddField(
            model_name='branchbuses',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='booker.bus'),
        ),
    ]
