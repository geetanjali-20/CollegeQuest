# Generated by Django 4.1.1 on 2022-09-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Auth', models.CharField(max_length=122)),
                ('Title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
