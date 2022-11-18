# Generated by Django 4.1 on 2022-11-18 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectroCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.TextField()),
                ('car_number', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('avatar', models.ImageField(upload_to='avatars')),
                ('birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('Ж', 'Женский')], max_length=10)),
                ('list_cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.electrocar')),
            ],
        ),
    ]
