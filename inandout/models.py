import pickle
import base64

import datetime as datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from oauth2client.django_orm import FlowField
from oauth2client.django_orm import CredentialsField

from tinymce.models import HTMLField



class CredentialsModel(models.Model):
  id = models.ForeignKey(User, primary_key=True)
  credential = CredentialsField()


class CredentialsAdmin(admin.ModelAdmin):
    pass


# admin.site.register(CredentialsModel, CredentialsAdmin)






class Product(models.Model):
    """ """
    brand = models.ForeignKey('Brand',
                            verbose_name="Which Brand does this belong to?",
                            related_name='brand',
                            blank=True, null=True)
    is_active = models.BooleanField("If unchecked, Product will not display on website",
                            default=False)
    frontpage = models.BooleanField("If Checked, Product will display on Front Page",
                            default=False)
    priority = models.IntegerField("Determines Priorty on the Front Page. Higher numbers show higher on the Front Page.",
                                    default=1)
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    short_name = models.CharField("Short field used on Product List page",
                            max_length=80)
    long_name = models.CharField("Longer name appended to short name",
                            max_length=200,
                            default="")
    price = models.DecimalField("Price of the Product.",
                            default="0.00",
                            max_digits=7,
                            decimal_places=2)
    long_text = models.CharField("A long description of the product, paragraphs OK",
                            max_length=2000)
    amazon_link = models.URLField("Amazon link to the Products purchase page",
                            max_length=300,
                            default="")
    main_image = models.ImageField("Image for the product. Should be as 'square' as possible",
                            upload_to = 'product_folder/', 
                            default = 'None/no-img.png')
    background_image = models.ImageField("Background image fr product display.",
                            upload_to = 'product_folder/', 
                            default = 'None/no-back-img.png')
    background_and_text_color = models.CharField("Background and Text Color. Use HTML acceptable names or Hex Code.",
                            max_length=20,
                            default='green')
    info_button_text = models.CharField("Text for the button that drops down the long text. (Overflows after ~14 characters)",
                            max_length=30,
                            default="Learn More")
    purchase_button_text = models.CharField("Text for the button that links to Amazon.  (Overflows after ~14 characters)",
                            max_length=30,
                            default="Buy at Amazon!")
    def __unicode__(self):              # __unicode__ on Python 2
        return self.short_name
    def type(self):
        return "Product"   

class Brand(models.Model):
    """ """
    is_active = models.BooleanField("If unchecked, Brand will not display on website",
                            default=False)
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    priority = models.IntegerField("Determines Priorty. Higher numbers show higher in list.",
                                    default=1)
    short_name = models.CharField("Brand Name",
                            max_length=80)    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.short_name    

class Blog(models.Model):
    """ """
    is_active = models.BooleanField("If unchecked, Blog will not display on website",
                            default=False)
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    frontpage = models.BooleanField("If Checked, Blog will display on Front Page",
                            default=False)
    priority = models.IntegerField("Determines Priorty on the Front Page. Higher numbers show higher on the Front Page.",
                                    default=1)
    title = models.CharField("Blog's title",
                            max_length=80)
    preview_text = models.CharField("Short preview shown in Blog list page",
                            max_length=160)
    # long_text = models.CharField("The main text of the Blog",
    #                         max_length=4000)
    html_text = HTMLField("The main text of the Blog",
                            max_length=4000)
    author = models.CharField("Author's visible name.",
                                    max_length=200,
                                    default=' ')
    fb_author_link = models.CharField("Facebook API - Link to Author's Facebook Page.",
                                    max_length=200,
                                    default=' ')
    main_image = models.ImageField("Image for the blog. Should be a wide rectangle, if possible",
                            upload_to = 'blog_folder/', 
                            default = 'None/no-img.png')
    preview_image = models.ImageField("Preview Image shown on the Index page.",
                            upload_to = 'blog_folder/', 
                            default = 'None/no-img.png')
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title
    def type(self):
        return "Blog"  

class Testamonial(models.Model):
    """ """
    is_active = models.BooleanField("If unchecked, Testamonial will not display on website",
                            default=False)
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    frontpage = models.BooleanField("If Checked, Testamonial will display on Front Page",
                            default=False)
    priority = models.IntegerField("Determines Priorty on the Front Page. Higher numbers show higher on the Front Page.",
                                    default=1)
    email_address = models.EmailField("Email address of submitter",
                            blank=True)
    text = models.CharField("Testamonial text",
                            max_length=400)
    nickname = models.CharField("Nickname of submitter",
                            max_length=80)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.nickname
    def type(self):
        return "Testamonial"  












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
    site_title = models.CharField("Title to be shown on Browser.",
                                    max_length=80,
                                    default='default CMS title.')
    testamonials_toggle = models.BooleanField("If unchecked, Testamonials will not display on menu bar.",
                            default=False)
    disclaimer_text = models.CharField("Disclaimer Text to show on all pages.",
                                    max_length=2000,
                                    default='default disclaimer text.')
    disclaimer_background_color = models.CharField("Disclaimer Background Color. Use HTML acceptable names or Hex Code.",
                                    max_length=20,
                                    default='#555')
    disclaimer_text_color = models.CharField("Disclaimer Text Color. Use HTML acceptable names or Hex Code.",
                                    max_length=20,
                                    default='#ccc')
    background_image = models.ImageField("Image for the Background.",
                            upload_to = 'basepage_folder/', 
                            default = 'None/no-img.png')
    banner_image = models.ImageField("Top of page Banner Image.",
                            upload_to = 'basepage_folder/', 
                            default = 'None/no-img.png')
    main_text_color = models.CharField("Main Text Color. Use HTML acceptable names or Hex Code.",
                                    max_length=60,
                                    default='orange')
    main_border_color = models.CharField("Main Border Color. Use HTML acceptable names or Hex Code.",
                                    max_length=60,
                                    default='orange')
    link_hover_color = models.CharField("Link Hover Color. Use HTML acceptable names or Hex Code.",
                                    max_length=60,
                                    default='orange')
    menu_bar_color = models.CharField("Menu Bar Color. Use HTML acceptable names or Hex Code.",
                                    max_length=60,
                                    default='#1d5065')
    menu_accent_color = models.CharField("Menu Accent Color. Use HTML acceptable names or Hex Code.",
                                    max_length=60,
                                    default='#3d7085')
    menu_background_color = models.CharField("Menu Background Color. Use HTML acceptable names or Hex Code.",
                                    max_length=60,
                                    default='#ccc')
    site_name = models.CharField("Facebook API - site name.",
                                    max_length=80,
                                    default='')
    site_desc = models.CharField("Facebook API - site description default value.",
                                    max_length=200,
                                    default='')
    fb_app_id = models.CharField("Facebook API - App ID.",
                                    max_length=200,
                                    default='')
    fb_page_link = models.CharField("Facebook API - Link to company Facebook Page.",
                                    max_length=200,
                                    default='')
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
    THIRDS = 270
    HALF = 420
    FULL = 870 ###
    WIDTH_CHOICES = (
        (THIRDS, 'Thirds'),
        (HALF, 'Half'),
        (FULL, 'Full'),
    )
    width = models.IntegerField("Set Size (Width) for Object. Be sure that complementary objects exist to prevent issues!",
                                    choices=WIDTH_CHOICES,
                                    default=HALF)
    title = models.CharField("Title to appear on admin page.",
                                    max_length=80,
                                    default="delete this to add title.")
    priority = models.IntegerField("Higher numbers show higher on the page.",
                                    default=0)
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
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

class PageObjectLink(models.Model):   
    """ """
    parent = models.ForeignKey('PageObject',
                                verbose_name="Which PageObject does this belong to?",
                                related_name='links')
    is_youtube = models.BooleanField("Check this if link is a youtube video!",
                            default=False)
    link = models.URLField("Link to appear in this object.",
                            max_length=300,
                            default="")
    def __unicode__(self):              # __unicode__ on Python 2
        return "Page Object Image"  
    def embed(self):
        return self.link.replace('watch?v=','embed/')   

class PageObjectHTML(models.Model):   
    """ """
    parent = models.ForeignKey('PageObject',
                                verbose_name="Which PageObject does this belong to?",
                                related_name='htmls')
    content = HTMLField("This will override all other Page Object components!",
                                    max_length=4000,
                                    default="")
    def __unicode__(self):              # __unicode__ on Python 2
        return "Page Object HTML"     

    # class Meta:
    #     verbose_name_plural = "FrontPage"   ###     

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    # question = models.ForeignKey(Question)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0) ##