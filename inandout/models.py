import pickle
import base64

import datetime as datetime

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
    brand = models.ForeignKey('Brand',
                                verbose_name="Which Brand does this belong to?",
                                related_name='brand',
                                blank=True, null=True)
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

class Brand(models.Model):
    """ """
    is_active = models.BooleanField("If unchecked, Brand will not display on website",
                            default=False)
    short_name = models.CharField("Brand Name",
                            max_length=80)    
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
    disclaimer_text = models.CharField("Disclaimer Text to show on all pages.",
                                    max_length=2000,
                                    default='default disclaimer text.')
    background_image = models.CharField("Background Image for entire website",
                                    max_length=200,
                                    default='inandout/images/background_1920x1084.png')
    link_hover_color = models.CharField("Link Hover Color. Use HTML acceptable names or Hex Code.",
                                    max_length=60,
                                    default='orange')
    def __unicode__(self):              # __unicode__ on Python 2
        return "Base Page (aka Whole Site) Content" 
    class Meta:
        verbose_name_plural = "BasePage"  ###




class PageObject(models.Model):   
    """ """
    is_active = models.BooleanField("If unchecked, Object will not display on website",
                            default=False)
    PAGE_CHOICES = (
        ('FP', 'Front Page (Home)'),
        ('AU', 'About Us'),
        ('CT', 'Contact'),
    )
    page = models.CharField("Which Page should this object display on?",
                                max_length=2, 
                                choices=PAGE_CHOICES,
                                default='FP')
    title = models.CharField("Title to appear on admin page.",
                                    max_length=80,
                                    default="delete this to add title.")
    priority = models.IntegerField("Higher numbers show higher on the page.",
                                    default=0)
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    width = models.IntegerField("420 for half page, 270 for thirds, 880 for full. Be sure that complementary objects exist to prevent issues!",
                                    default=420)
    def __unicode__(self):              # __unicode__ on Python 2
        return "Page Object" 

class PageObjectText(models.Model):   
    """ """
    parent = models.ForeignKey('PageObject',
                                verbose_name="Which PageObject does this belong to?",
                                related_name='texts')
    text = models.CharField("Text to appear in this object.",
                                    max_length=400,
                                    default="delete this to add text.")
    def __unicode__(self):              # __unicode__ on Python 2
        return "Page Object Text" 

class PageObjectImage(models.Model):   
    """ """
    parent = models.ForeignKey('PageObject',
                                verbose_name="Which PageObject does this belong to?",
                                related_name='images')
    image = models.ImageField("Image to appear in this object.")
    def __unicode__(self):              # __unicode__ on Python 2
        return "Page Object Image" 

    # class Meta:
    #     verbose_name_plural = "FrontPage"        

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    # question = models.ForeignKey(Question)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0) ##