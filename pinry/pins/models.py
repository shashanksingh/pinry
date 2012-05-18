from django.db import models
from django.template.defaultfilters import slugify
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib.auth.models import User
#from thumbs import ImageWithThumbsField

import urllib2


class Pin(models.Model):
    url = models.TextField()
    description = models.TextField(blank=True, null=True)
#    image = ImageWithThumbsField(upload_to='pins/pin', sizes=((200,1000),))
    image = models.ImageField(upload_to='pins/pin')
    is_video = models.BooleanField()
    blog_url = models.URLField(blank=True,null=True)
    buy_url = models.URLField(blank=True,null=True)
    author = models.ForeignKey(User)
    

    def __unicode__(self):
        return self.url

    def save(self):
        if not self.image:
            temp_img = NamedTemporaryFile()
            temp_img.write(urllib2.urlopen(self.url).read())
            temp_img.flush()
            self.image.save(self.url.split('/')[-1], File(temp_img))
        super(Pin, self).save()
