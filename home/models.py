from django.db import models




class Emp(models.Model):
    Name= models.CharField(max_length=1000)
    Address=models.TextField()
    email= models.EmailField( max_length=254)
    Postion=models.CharField(max_length=200,choices=(('Clerk','Clerk'),('Manager','Manager'),('Devloper','Devloper'),('Other','Other')))
    
    
