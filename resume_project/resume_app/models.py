from django.db import models

# Create your models here.
class Resume(models.Model):
    # user_profile=models.ImageField(blank=True,null=True,upload_to='images/')
    Name=models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    careerObj = models.CharField(max_length=100,null=True,blank=True)

    # company=models.CharField(max_length=100,null=True,blank=True)
    collegeName=models.CharField(max_length=100,null=True,blank=True)
    course=models.CharField(max_length=100,null=True,blank=True)
    year_of_pass=models.DateField(null=True,blank=True)
    percentage=models.IntegerField(null=True,blank=True)
    project=models.CharField(max_length=100,null=True,blank=True)

    technical_skills=models.CharField(max_length=100,null=True,blank=True)
    profile=models.CharField(max_length=100,null=True,blank=True)
    company=models.CharField(max_length=100,null=True,blank=True)

    address=models.CharField(max_length=100,null=True,blank=True)

