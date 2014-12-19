from django.db import models


# Create your models here.


class Product(models.Model):
    long_text = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.long_text



# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    # question = models.ForeignKey(Question)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)