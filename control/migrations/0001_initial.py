# Generated by Django 4.0.2 on 2022-08-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('echipa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
    ]
