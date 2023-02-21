from django.db import models

class EnModel(models.Model):
    name = models.CharField(max_length=40)
    phone = models.IntegerField()
    subject = models.CharField(max_length=40)

    def _str_(self):
        return self.name + " " + self.subject + " " 