from django.db import models

# null--> database | blank--> user/client


class Advocate(models.Model):
    company = models.ForeignKey(
        'Company', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=500, null=True)
    profile_pic = models.URLField(max_length=500, null=True)
    username = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.username)


class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)
