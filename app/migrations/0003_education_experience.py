# Generated by Django 4.1.3 on 2022-11-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100, verbose_name='コース')),
                ('school', models.CharField(max_length=100, verbose_name='学校')),
                ('place', models.CharField(max_length=100, verbose_name='場所')),
                ('period', models.CharField(max_length=100, verbose_name='期間')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=100, verbose_name='職種')),
                ('company', models.CharField(max_length=100, verbose_name='会社')),
                ('description', models.TextField(verbose_name='説明')),
                ('place', models.CharField(max_length=100, verbose_name='場所')),
                ('period', models.CharField(max_length=100, verbose_name='期間')),
            ],
        ),
    ]
