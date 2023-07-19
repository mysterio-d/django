from django.db import models

# Create your models here.
class departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_decription = models.TextField()
    
    def __str__(self):
        return self.dep_name
    
    
class Doce(models.Model):
    docs_name =models.CharField(max_length=225,default='Docs_name') 
    doc_spec  =models.CharField(max_length=255)
    dep_name  =models.ForeignKey(departments,on_delete=models.CASCADE)
    doc_image =models.ImageField(upload_to='doctors')
    
    
    def __str__(self):
        return 'Dr.' + self.docs_name + '-  ('+ self.doc_spec + ')'
       
class Booking(models.Model):
    p_name =models.CharField(max_length=255,default='Patient_name')
    p_phone =models.CharField(max_length=10)
    p_email =models.EmailField()
    docs_name =models.ForeignKey(Doce, on_delete=models.CASCADE)
    booking_date =models.DateField()
    booked_on =models.DateField(auto_now=True)
    
    
    
class Book(models.Model):
    p_nam =models.CharField(max_length=255,default='Patient_nam')
     
    
   
    

       


    