# Generated by Django 3.2.6 on 2023-05-30 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0006_auto_20230529_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='pret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
