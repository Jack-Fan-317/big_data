from django.db import models

# Create your models here.
class Weblogs(models.Model):
    id = models.AutoField(primary_key=True)
    datatime = models.CharField(max_length=20)
    userid = models.CharField(max_length=255)
    searchname = models.CharField(max_length=255)
    retorder = models.CharField(max_length=255)
    cliorder = models.CharField(max_length=255)
    cliurl = models.CharField(max_length=255)


class WeblogsSmall(models.Model):
    id = models.AutoField(primary_key=True)
    datatime = models.CharField(max_length=20)
    userid = models.CharField(max_length=255)
    searchname = models.CharField(max_length=255)
    retorder = models.CharField(max_length=255)
    cliorder = models.CharField(max_length=255)
    cliurl = models.CharField(max_length=255)


class WebCount(models.Model):
    searchname = models.CharField(max_length=255,primary_key=True)
    count = models.IntegerField()
    