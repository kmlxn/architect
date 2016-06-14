from django.db import models


class ProjectTag(models.Model):
    caption = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.caption

    def get_data(self):
        return {
            'alias': self.alias,
            'caption': self.caption,
        }

class Project(models.Model):
    picture = models.ImageField(upload_to='projects')
    caption = models.CharField(max_length=255)
    tag = models.ManyToManyField(ProjectTag)

    def __str__(self):
        return self.caption

    def get_data(self):
        return {
            'picture': self.picture.url,
            'caption': self.caption,
        }


class ContactInfo(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

    def get_data(self):
        return {
            'text': self.text,
        }
