from django.db import models
import re
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    craeted = models.DateTimeField(auto_now=True)

    class Meta(AbstractUser.Meta):
        swappable  = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img_logo = models.ImageField(upload_to='partnership_logo/', validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_-]+\.(jpg|jpeg|png|gif)$',
            message='File name must have a valid image extension (jpg, jpeg, png, gif).',
            code='invalid_image_filename'
        ),
    ])
    banner_img = models.ImageField(upload_to='banner_photo/', validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_-]+\.(jpg|jpeg|png|gif)$',
            message='File name must have a valid image extension (jpg, jpeg, png, gif).',
            code='invalid_image_filename'
        ),
    ])
    craeted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Recomendation(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='Recomendation_photo/')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user_img = models.ImageField(upload_to='user_photo/', validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_-]+\.(jpg|jpeg|png|gif)$',
            message='File name must have a valid image extension (jpg, jpeg, png, gif).',
            code='invalid_image_filename'
        ),
    ])
    CHOICES_TAG = (
        ('popular', 'popular'),
        ('new house', 'new house'),
        ('best deals', 'best deals'),
    )
    tag = models.CharField(max_length=25, choices=CHOICES_TAG)
    CHOICES_TYPE = (
        ('house', 'house'),
        ('villa', 'villa'),
        ('apartment', 'apartment'),
    )
    type = models.CharField(max_length=25, choices=CHOICES_TYPE)
    craeted = models.DateTimeField(auto_now=True)




class Sell(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    detail = models.ManyToManyField(to='Detail')
    user_img = models.ImageField(upload_to='user_photo/', validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_-]+\.(jpg|jpeg|png|gif)$',
            message='File name must have a valid image extension (jpg, jpeg, png, gif).',
            code='invalid_image_filename'
        ),
    ])
    user_name = models.CharField(max_length=255)
    user_job = models.CharField(max_length=255)
    presintation = models.ManyToManyField(to='Presintaiton')
    craeted = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Detail(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    craeted = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Presintaiton(models.Model):
    img = models.FileField(upload_to='photo_vidoe/', validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_-]+\.(jpg|jpeg|png|gif|mp4|mov|avi)$',
            message='File name must have a valid image or video extension (jpg, jpeg, png, gif, mp4, mov, avi).',
            code='invalid_file_extension'
        ),
    ])
    craeted = models.DateTimeField(auto_now=True)



class Testimonial(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='testimonail_img/', validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_-]+\.(jpg|jpeg|png|gif)$',
            message='File name must have a valid image extension (jpg, jpeg, png, gif).',
            code='invalid_image_filename'
        ),
    ])

    user_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user_img = models.ImageField(upload_to='user_img/', validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_-]+\.(jpg|jpeg|png|gif)$',
            message='File name must have a valid image extension (jpg, jpeg, png, gif).',
            code='invalid_image_filename'
        ),
    ])
    user_job = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    reting = models.FloatField()
    craeted = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user_name


class About_us(models.Model):
    title = models.CharField(max_length=255)
    user_fullname = models.CharField(max_length=255)
    img = models.ImageField(upload_to='house_img/', validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_-]+\.(jpg|jpeg|png|gif)$',
            message='File name must have a valid image extension (jpg, jpeg, png, gif).',
            code='invalid_image_filename'
        ),
    ])

    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_fullname


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
            message='Enter a valid email address.',
            code='invalid_email'
        ),
    ])
    craeted = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Info(models.Model):
    my_logo = models.ImageField(upload_to='my_logo/', validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_-]+\.(jpg|jpeg|png|gif)$',
            message='File name must have a valid image extension (jpg, jpeg, png, gif).',
            code='invalid_image_filename'
        ),
    ])

    description = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    email = models.CharField(max_length=100, validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
            message='Enter a valid email address.',
            code='invalid_email'
            ),
        ])
    craeted = models.DateTimeField(auto_now=True)






