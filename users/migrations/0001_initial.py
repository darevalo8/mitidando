# Generated by Django 3.0.3 on 2020-07-03 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, verbose_name='Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, verbose_name='País')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(max_length=12, verbose_name='Documento')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.City')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deparment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deparment_name', models.CharField(max_length=50, verbose_name='Departamento')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='deparment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Deparment'),
        ),
    ]
