from django.db import models
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    system_design = models.TextField()
    working_principle = models.TextField()
    workflow = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
