from django.db import models

# Create your models here.


class StudentModel(models.Model):
    rno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
