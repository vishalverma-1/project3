from django.db import models

class company(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    def __str__(self):
        return self.name
    
