from django.db import models

# Create your models here.
class FbModel(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
