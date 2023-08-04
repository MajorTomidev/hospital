from django.db import models

# Create your models here.
class Hospital (models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='hospital_images')
    license_number = models.CharField(max_length=100)
    number_of_staff = models.IntegerField()
    years_in_operation = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Hospital')
        verbose_name_plural = ('Hospitals')

class History (models.Model):
    pass

class Patient (models.Model):
    name = models.CharField(max_length=100, blank=False )
    age = models.CharField(max_length=10, blank=False )
    gender = models.CharField(max_length=10, blank=False)
    email = models.EmailField()
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Patient')
        verbose_name_plural = ('Patients')

