from django.db import models

from django.db.models.aggregates import Count
from random import randint
import random

from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


class nouns(models.Model):
    id = models.AutoField(primary_key=True)
    eng = models.CharField(max_length=100)
    fr = models.CharField(max_length=100)
    img_photo = models.ImageField(upload_to='images/',null=True, blank=True)
    pass

    
    def __str__(self):
        return self.eng

    def random_item(self):
        s=nouns.objects.order_by('?').first()
        return s
    
    def storeRand(self):
        s=nouns.random_item(self)
        d=s
        return d
    
    @property
    def photo_url(self):     #{{ noun.photo_url|default_if_none:'#'}}
        if self.img_photo and hasattr(self.img_photo, 'url'):
            return self.img_photo.url
    




class verbs(models.Model):
    
    
    id = models.AutoField(primary_key=True)
    eng = models.CharField(max_length=100)
    fr = models.CharField(max_length=100)
    img_photo = models.ImageField(upload_to='images/',null=True, blank=True)
    pass

    
    def __str__(self):
        return self.eng

    def random_item(self):
        s=nouns.objects.order_by('?').first()
        return s
    
    def storeRand(self):
        s=nouns.random_item(self)
        d=s
        return d
    
    @property
    def photo_url(self):     #{{ noun.photo_url|default_if_none:'#'}}
        if self.img_photo and hasattr(self.img_photo, 'url'):
            return self.img_photo.url
    
#class Images(models.Model):

#img_photo = models.ImageField(upload_to='images/',null=True, blank=True)

#def get_image(self):
#    if self.img_photo and hasattr(self.img_photo, 'url'):
#        return self.img_photo.url
#    else:
#        return '/media/images/accident.png'

#def __str__(self):
#    return self.img_photo






class cross(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=100)
    pass

    
    def __str__(self):
        return self.word

    