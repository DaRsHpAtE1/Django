from django.db import models

class StudentModel(models.Model):
    rno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    ms = models.ImageField()
    def __str__(self):
        return str(self.rno)+" "+str(self.name)