# Generated by Django 4.1.1 on 2022-09-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('idade', models.PositiveIntegerField(max_length=3)),
                ('cidade', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
    ]
