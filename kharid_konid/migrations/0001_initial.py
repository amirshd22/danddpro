# Generated by Django 2.0.2 on 2019-03-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kharid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('text', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=55)),
                ('date', models.DateField()),
            ],
        ),
    ]