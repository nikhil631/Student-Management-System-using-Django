from django.db import models

# Create your models here.
class studs(models.Model):
    name=models.CharField(max_length=400)
    roll=models.AutoField(primary_key=True,unique=True)
    email=models.EmailField(max_length=254,null=True,unique=True)
    def __str__(self):
        return f"{self.roll} , {self.name} , {self.email}"
class attendance(models.Model):
    roll=models.ForeignKey(studs,to_field="roll",on_delete=models.CASCADE)
    date=models.DateField()
    attend=models.BooleanField(default=False)