from django.db import models
from django.contrib.auth.models import User
import datetime
from settings import settings

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User)
    friends = models.ManyToManyField("self", blank=True)

    def __unicode__(self):
        return self.user.username

class PlantImageZipFile(models.Model):
    image_base = models.CharField(max_length=100)
    file = models.FileField(upload_to="plant_zips/")

    def save(self, *args, **kwargs):
        super(PlantImageZipFile, self).save(*args, **kwargs)
        import sys, zipfile, os, os.path
        #path = self.file.filename
        thefile = self.file

        # Convert file and dir into absolute paths
        fullpath = os.path.join(settings.MEDIA_ROOT,thefile.name)
        dirname = os.path.dirname(fullpath)

        # Get a real Python file handle on the uploaded file
        fullpathhandle = open(fullpath, 'r')

        # Unzip the file, creating subdirectories as needed
        zfobj = zipfile.ZipFile(fullpathhandle)
        for name in zfobj.namelist():
            if name.endswith('/'):
                try: # Don't try to create a directory if exists
                    os.mkdir(os.path.join(dirname, name))
                except:
                    pass
            else:
                outfile = open(os.path.join(dirname, name), 'wb')
                outfile.write(zfobj.read(name))
                outfile.close()

        # Now try and delete the uploaded .zip file and the
        # stub __MACOSX dir if they exist.
        try:
            os.remove(fullpath)
        except:
            pass

        try:
            osxjunk = os.path.join(dirname,'__MACOSX')
            shutil.rmtree(osxjunk)
        except:
            pass

    def __unicode__(self):
        return self.image_base

class PlantType(models.Model):
    name = models.CharField(max_length=100)
    sample_image = models.ImageField(upload_to="plant_type_samples/")
    piece_image = models.ImageField(upload_to="plant_type_pieces/")
    imagezip = models.OneToOneField(PlantImageZipFile)

    def __unicode__(self):
        return self.name

class PressDate(models.Model):
    press_date = models.DateField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.press_date

class Timeline(models.Model):
    plant_name = models.CharField(max_length=100, null=True)
    press_date = models.ManyToManyField(PressDate)

    def __unicode__(self):
        return self.plant_name or ''

class Background(models.Model):
    background_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="backgrounds/")
    promo_image = models.ImageField(upload_to="promo_images/")

    def __unicode__(self):
        return self.background_name

class Pot(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pots/")


class UserPlant(models.Model):
    name = models.CharField(max_length=100)
    last_press = models.DateField(auto_now=False, auto_now_add=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    type = models.ForeignKey(PlantType)
    owner = models.ForeignKey(Player)
    timeline = models.OneToOneField(Timeline)
    background = models.ForeignKey(Background)
    day_num = models.IntegerField(default=0)
    pot = models.ForeignKey(Pot)

    def save(self, *args, **kwargs):
        if not self.id:
            pressdatenow = PressDate()
            pressdatenow.save()
            new_timeline = Timeline(plant_name=self.name)
            new_timeline.save()
            new_timeline.press_date.add(pressdatenow)
            new_timeline.save()
            self.timeline = new_timeline
        super(UserPlant, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
