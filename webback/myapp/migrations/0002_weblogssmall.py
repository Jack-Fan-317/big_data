# Generated by Django 2.2.1 on 2021-03-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeblogsSmall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datatime', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=255)),
                ('searchname', models.CharField(max_length=255)),
                ('retorder', models.CharField(max_length=255)),
                ('cliorder', models.CharField(max_length=255)),
                ('cliurl', models.CharField(max_length=255)),
            ],
        ),
    ]
