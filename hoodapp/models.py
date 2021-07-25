from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField
from url_or_relative_url_field.fields import URLOrRelativeURLField

# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='admin')
    hoodimage = CloudinaryField()
    description = HTMLField()
    police_number = models.IntegerField(null=True, blank=True)
    emergency_no = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_hood(self):
        self.save()

    def update_hood(self):
      self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    bio = HTMLField(max_length=100)
    profile_pic = CloudinaryField(
        default="https://res.cloudinary.com/playboard/image/upload/v1626529829/vjytnast5wblft8xvy9p.jpg",
    )
    full_name = models.CharField(blank=True, max_length=120)
    profession = models.CharField(blank=True, max_length=120)
    email_address = models.EmailField(null=True, blank=True)
    website = URLOrRelativeURLField(null=True,blank=True)
    facebook =URLOrRelativeURLField(null=True,blank=True)
    instagram = URLOrRelativeURLField(null=True,blank=True)
    twitter = URLOrRelativeURLField(null=True,blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Hood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return self.user


class Business(models.Model):
    bs_name= models.CharField(max_length=100, null=False, blank=False)
    description = HTMLField(blank=True)
    bs_logo = CloudinaryField(blank =False, null = False)
    owner = models.ForeignKey(Profile, null=False, blank=False, on_delete=models.CASCADE, related_name='owner')
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE, related_name='business')
    bs_email = models.EmailField(null=False, blank=True)
    facebook =URLOrRelativeURLField(null=True,blank=True)
    instagram = URLOrRelativeURLField(null=True,blank=True)
    twitter = URLOrRelativeURLField(null=True,blank=True)

    def __str__(self):
        return str(self.bs_name)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    details = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='hood_post')

    def __str__(self):
        return f'{self.title} post'

    def new_post(self):
        self.save()

    def delete_post(self):
        self.delete()