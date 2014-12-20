from django.db import models


# Create your models here.


class Product(models.Model):
    is_active = models.BooleanField(default=False)
    short_name = models.CharField(max_length=80)
    long_name = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to = 'product_folder/', default = 'product_folder/None/no-img.jpg')
    long_text = models.CharField(max_length=2000)
    amazon_link = models.URLField(max_length=300,default="")
    def __unicode__(self):              # __unicode__ on Python 2
        return self.short_name

class Blog(models.Model):
    is_active = models.BooleanField(default=False)
    title = models.CharField(max_length=80)
    preview_text = models.CharField(max_length=160)
    main_image = models.ImageField()
    long_text = models.CharField(max_length=4000)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

class Testamonial(models.Model):
    is_active = models.BooleanField(default=False)
    email_address = models.EmailField(blank=True)
    text = models.CharField(max_length=400)
    nickname = models.CharField(max_length=80)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.nickname

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    # question = models.ForeignKey(Question)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)