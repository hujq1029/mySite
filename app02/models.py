from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=64,blank=True,null=True)
    password = models.CharField(max_length=64,blank=True,null=True)
    hobby = models.ForeignKey('Hobby',blank=True,null=True)

    class Meta:
        db_table = 'userinfo'

    def __str__(self):
        return self.username


class Hobby(models.Model):
    name = models.CharField(max_length=64,blank=True,null=True)

    class Meta:
        db_table = 'hobby'

    def __str__(self):
        return self.name