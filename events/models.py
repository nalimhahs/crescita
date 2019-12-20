from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.


class Catagory(models.Model):

    name = models.CharField(max_length=32)
    desc = models.TextField(max_length=128, null=True)
    thumbnail = models.ImageField()
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.event_slug = slugify(self.name)

        super(Catagory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Organizer(models.Model):

    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Event(models.Model):

    name = models.CharField(max_length=64)
    desc = models.TextField(max_length=4000)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    organizer_1 = models.ForeignKey(
        Organizer, on_delete=models.PROTECT, related_name='event_organizer_1', null=True, blank=True)
    organizer_2 = models.ForeignKey(
        Organizer, on_delete=models.PROTECT, related_name='event_organizer_2', null=True, blank=True)
    event_start = models.DateTimeField(null=True, blank=True)
    event_end = models.DateTimeField(null=True, blank=True)
    banner_image = models.ImageField()
    catagory = models.ForeignKey(
        Catagory, on_delete=models.PROTECT, null=True, blank=True)
    reg_link = models.URLField(null=True, blank=True)
    event_slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.event_slug = slugify(self.name)

        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
