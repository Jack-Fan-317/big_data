# Generated by Django 2.2.1 on 2021-03-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weblogs',
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
