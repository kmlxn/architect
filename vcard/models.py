from django.db import models



class Project(models.Model):
    picture = models.ImageField(upload_to='projects')
    caption = models.CharField(max_length=255)



class ContactInfo(models.Model):
    text = models.CharField(max_length=255)



class TextOnSite(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
