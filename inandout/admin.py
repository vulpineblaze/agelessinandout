from django.contrib import admin

from inandout.models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Testamonial)




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