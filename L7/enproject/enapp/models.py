from django.db import models


class EnModel(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    course = models.CharField(max_length=100)
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name