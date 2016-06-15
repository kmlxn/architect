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
    caption = models.CharField(max_length=255)
    url_name = models.CharField(max_length=255, unique=True)
    tag = models.ManyToManyField(ProjectTag)

    def __str__(self):
        return self.caption

    def get_data(self):
        pictures_as_orm = self.pictures.order_by('order')

        return {
            'caption': self.caption,
            'url_name': self.url_name,
            'pictures': [pic.get_data() for pic in pictures_as_orm],
        }


class ProjectPicture(models.Model):
    picture = models.ImageField(upload_to='projects')
    order = models.IntegerField(default=0)
    project = models.ForeignKey(Project, related_name='pictures')

    def get_data(self):
        return {
            'url': self.picture.url,
            'order': self.order,
        }


class ContactInfo(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

    def get_data(self):
        return {
            'text': self.text,
        }
