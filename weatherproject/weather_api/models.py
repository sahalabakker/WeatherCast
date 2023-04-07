from django.db import models

# Create your models here.

# class Social(models.Model):
#     website_url = models.CharField(max_length=255, null=True, blank=True)
#     facebook_url = models.CharField(max_length=255, null=True, blank=True)
#     instagram_url = models.CharField(max_length=255, null=True, blank=True)
#     twitter_url = models.CharField(max_length=255, null=True, blank=True)
#     github_url = models.CharField(max_length=255, null=True, blank=True)
#     linkedin_url = models.CharField(max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return self.website_url
class Reg(models.Model):
    finame=models.CharField(max_length=20)
    laname=models.CharField(max_length=20)
    email=models.EmailField()
    area=models.CharField(max_length=30)
    phone=models.IntegerField()
    pswrd=models.CharField(max_length=50)