# Generated by Django 2.2.1 on 2021-03-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_weblogssmall'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebCount',
            fields=[
                ('searchname', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
