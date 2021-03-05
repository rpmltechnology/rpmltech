from django.db import models

# Create your models here.
class Header(models.Model):
    logo=models.ImageField(upload_to="logo",blank=False)
    main_body_img=models.ImageField(upload_to="images",blank=False)
    title_body=models.CharField(max_length=256,blank=False)
    title_icon=models.ImageField(upload_to="icons",blank=False)
    trending_title=models.CharField(max_length=20,blank=True)
    trending_image=models.ImageField(upload_to="trending",blank=True)
    trending_discription=models.CharField(max_length=100,blank=True)

    def __str(self):
        return self.title_body

class Acheivement(models.Model):
    Total_no_of_client=models.IntegerField(blank=False)
    Trusted=models.IntegerField(blank=False)
    Locations=models.IntegerField(blank=False)
    Consulting_services=models.IntegerField(blank=False)

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject=models.CharField(max_length=200)
    message = models.TextField()
