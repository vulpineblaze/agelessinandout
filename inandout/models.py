import pickle
import base64

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from oauth2client.django_orm import FlowField
from oauth2client.django_orm import CredentialsField


class CredentialsModel(models.Model):
  id = models.ForeignKey(User, primary_key=True)
  credential = CredentialsField()


class CredentialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(CredentialsModel, CredentialsAdmin)






class Product(models.Model):
    """ """
    is_active = models.BooleanField("If unchecked, Product will not display on website",
                            default=False)
    short_name = models.CharField("Short field used on Product List page",
                            max_length=80)
    long_name = models.CharField("Longer name used in Product detail apge",
                            max_length=200)
    main_image = models.ImageField("Image for the product. Should be as 'square' as possible",
                            upload_to = 'product_folder/', 
                            default = 'product_folder/None/no-img.jpg')
    long_text = models.CharField("A long description of the product, paragraphs OK",
                            max_length=2000)
    amazon_link = models.URLField("Amazon link to the Products purchase page",
                            max_length=300,
                            default="")
    def __unicode__(self):              # __unicode__ on Python 2
        return self.short_name

class Blog(models.Model):
    """ """
    is_active = models.BooleanField("If unchecked, Blog will not display on website",
                            default=False)
    title = models.CharField("Blog's title",
                            max_length=80)
    preview_text = models.CharField("Short preview shown in Blog list page",
                            max_length=160)
    main_image = models.ImageField("Image for the blog. Should be a wide rectangle, if possible"
                            )
    long_text = models.CharField("The main text of the Blog",
                            max_length=4000)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

class Testamonial(models.Model):
    """ """
    is_active = models.BooleanField("If unchecked, Testamonial will not display on website",
                            default=False)
    email_address = models.EmailField("Email address of submitter",
                            blank=True)
    text = models.CharField("Testamonial text",
                            max_length=400)
    nickname = models.CharField("Nickname of submitter",
                            max_length=80)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.nickname



class FrontPage(models.Model):   
    """ """
    main_text = models.CharField("Main text for the front page (aka Home)",
                                    max_length=4000,
                                    default='This is the default frontpage main text')
    def __unicode__(self):              # __unicode__ on Python 2
        return "Front Page Content" 
    class Meta:
        verbose_name_plural = "FrontPage"      

class BasePage(models.Model):   
    """ """
    background_image = models.CharField("Background Image for entire website",
                                    max_length=200,
                                    default='inandout/images/background_1920x1084.png')
    def __unicode__(self):              # __unicode__ on Python 2
        return "Base Page (aka Whole Site) Content" 
    class Meta:
        verbose_name_plural = "BasePage"  

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    # question = models.ForeignKey(Question)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0) ##