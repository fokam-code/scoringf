# Generated by Django 3.2.6 on 2023-05-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0005_auto_20230527_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(default='anonyme', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('describe', models.TextField(default='test')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='test',
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.RemoveField(
            model_name='client',
            name='files',
        ),
    ]
