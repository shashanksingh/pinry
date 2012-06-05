from django.db import models
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib.auth.models import User
from django.conf import settings
#from thumbs import ImageWithThumbsField

import urllib2


class Pin(models.Model):
    url = models.TextField()
    description = models.TextField(blank=True, null=True)
#    image = ImageWithThumbsField(upload_to='pins/pin', sizes=((200,1000),))
    image = models.ImageField(upload_to='pins/pin')
    is_video = models.BooleanField()
    similar_items = models.BooleanField()
    blog_url = models.URLField(blank=True,null=True)
    buy_url = models.URLField(blank=True,null=True)
    author = models.ForeignKey(User)
    #image = ImageWithThumbsField(upload_to='pins/pin', sizes=((200, 1000),))

    def __unicode__(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.image:
            temp_img = NamedTemporaryFile()
            temp_img.write(urllib2.urlopen(self.url).read())
            temp_img.flush()
            # pylint: disable-msg=E1101
            self.image.save(self.url.split('/')[-1], File(temp_img))
        super(Pin, self).save()
    
    def thumbnail(self):
        """
        Display thumbnail-size image of ImageField named src
        Assumes images are not very large (i.e. no manipulation of the image is done on backend)
        Requires constant named MAX_THUMB_LENGTH to limit longest axis
        """
        MAX_THUMB_LENGTH = 50
        #max_img_length = max(self.get_image_width(), self.get_image_height())
        #ratio = max_img_length > MAX_THUMB_LENGTH and float(max_img_length) / MAX_THUMB_LENGTH or 1
        #thumb_width = self.get_image_width() / ratio
        #thumb_height = self.get_image_height() / ratio
        #url = '%s%s' % (settings.ADMIN_MEDIA_PREFIX, self.image.url())
        return '<img src="%s"  height="%s"/>' % (self.image, 50)
    
    thumbnail.short_description = 'Image thumbnail'
    thumbnail.allow_tags = True
    
    def buy_url_exists(self):
       if self.buy_url:
           return True
       else:
           return False
    buy_url_exists.boolean = True
    
    def blog_url_exists(self):
       if self.blog_url:
           return True
       else:
           return False
    blog_url_exists.boolean = True

    class Meta:
        ordering = ['-id']
