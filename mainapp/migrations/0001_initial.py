# Generated by Django 4.1.3 on 2022-11-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=11, verbose_name='Имя')),
                ('l_name', models.CharField(max_length=21, verbose_name='Фамилия')),
            ],
        ),
    ]
