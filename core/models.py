from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
import random
from pathlib import Path
# Create your models here.



def path_and_rename(instance, filename):
    print("filename: ", filename)
    upload_to = 'pescription'
    ext = filename.split('.')[-1]
    # get filename
    i=1
    format = instance.user.username+"-"+str(i)+"."+ext
   
    if os.path.exists(format):
        print("File exists")
        #i += 1
        #print(i)
        #format = instance.user.username+"-"+str(i)+"."+ext
       
    return os.path.join(upload_to, format)



class Pescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nid = models.CharField(max_length=50)
# Create your models here.
    image = models.ImageField(upload_to=path_and_rename)

    def __str__(self) -> str:
        return self.nid

    # def save(self, *args, **kwargs):
    #     self.image = path_and_rename(self, self.image)
    #     super().save(*args, **kwargs)

    # def save(self):
    #     for field in self._meta.fields:
    #         if field.name == 'image':
    #             field.upload_to = 'photos/%d' % self.id
    #     super(Pescription, self).save()