from django.contrib import admin
#from django.forms.widgets import Textarea

from django import forms

from inandout.models import *

# Register your models here.





class ProductForm(forms.ModelForm):
    """ """
    class Meta:
        model = Product
        widgets = {
            'long_text':forms.Textarea
        }

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

admin.site.register(Product, ProductAdmin)



class BlogForm(forms.ModelForm):
    """ """
    class Meta:
        model = Blog
        widgets = {
            'long_text':forms.Textarea
        }

class BlogAdmin(admin.ModelAdmin):
    form = BlogForm

admin.site.register(Blog, BlogAdmin)



class TestamonialForm(forms.ModelForm):
    """ """
    class Meta:
        model = Testamonial
        widgets = {
            'text':forms.Textarea
        }

class TestamonialAdmin(admin.ModelAdmin):
    form = TestamonialForm

admin.site.register(Testamonial, TestamonialAdmin)



class FrontPageForm(forms.ModelForm):
    """ """
    class Meta:
        model = FrontPage
        widgets = {
            'main_text':forms.Textarea
        }
    # class Meta:
    #     model = Order
    #     widgets = {
    #         'activity': forms.Textarea(attrs={'disabled': True}),
    #         'log': forms.Textarea(attrs={'disabled': True}),
    #     }
 

class FrontPageAdmin(admin.ModelAdmin):
    form = FrontPageForm

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(FrontPage, FrontPageAdmin)






class BasePageAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.TextField: {'widget': RichTextEditorWidget},
    # }
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True
            
admin.site.register(BasePage, BasePageAdmin)



# # ####  Example to disable "Add" button
# # admin.py
# from django.contrib import admin
# from example.models import Example

# class ExampleAdmin(admin.ModelAdmin):
#   def has_add_permission(self, request):
#     num_objects = self.model.objects.count()
#     if num_objects >= 1:
#       return False
#     else:
#       return True

# admin.site.register(Example, ExampleAdmin)
# # #################### 