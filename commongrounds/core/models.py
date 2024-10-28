from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    file = models.ImageField(upload_to='images/')

class Userprofile(models.Model):
    name = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    bio = models.TextField()
    isConsultant = models.BooleanField(default=False)
    isVenueManager = models.BooleanField(default=False)

class Locality(models.Model):
    postcode = models.IntegerField(unique=True, primary_key=True)
    place_name = models.TextField()
    state_name = models.TextField()
    state_code = models.TextField()

class Address(models.Model):
    address_line_1 = models.TextField()
    address_line_2 = models.TextField()
    street_name = models.TextField()
    Locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    google_embed_link = models.URLField()

class Service(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('Resume Consultation', 'Resume Consultation'),
        ('Fitness Training', 'Fitness Training'),
        ('Board Games', 'Board Games'),
    ]
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    provider = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='services')
    description = models.TextField()
    rate = models.FloatField()
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)

class Venue(models.Model):
    venue_name = models.TextField()
    venue_images = models.ManyToManyField(Image)
    venue_manager = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='venues')
    description = models.TextField()
    rate = models.FloatField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Schedule(models.Model):
    consumer = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='events')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='events')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    day = models.DateTimeField()
