from django.db import models

class ViandType(models.Model):
    name = models.CharField(max_length=150)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name 

class Viand (models.Model):
    name = models.CharField(max_length=150)
    price= models.DecimalField(max_digits=7,decimal_places=2)
    type= models.ForeignKey(ViandType, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='viand/%Y/%m/%d/')
    ingredients=models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
