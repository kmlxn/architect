from django.db import models



class ProjectTag(models.Model):
    caption = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.caption



class Project(models.Model):
    picture = models.ImageField(upload_to='projects')
    caption = models.CharField(max_length=255)
    tag = models.ManyToManyField(ProjectTag)



class ContactInfo(models.Model):
    text = models.CharField(max_length=255)



class TextOnSite(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
