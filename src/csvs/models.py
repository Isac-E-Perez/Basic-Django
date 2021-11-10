from django.db import models

# Create your models here.

class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs/', max_length=100)
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return "File id: {}".format(self.id)
        
# the idea behind this field is that I am going to upload a file, but before I can create a 
# purchase objects from theh rows coming from the file that I uploaded
# we are going to grab the csv that is activated to false     
# When I succeed and create those objects, I am going to set the activated to True 

 