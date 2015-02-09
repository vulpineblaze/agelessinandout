# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inandout', '0007_auto_20150108_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info_button_text',
            field=models.CharField(default=b'Learn More', max_length=30, verbose_name=b'Text for the button that drops down the long text. (Overflows after ~14 characters)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_button_text',
            field=models.CharField(default=b'Buy at Amazon!', max_length=30, verbose_name=b'Text for the button that links to Amazon.  (Overflows after ~14 characters)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='long_name',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Longer name appended to short name'),
            preserve_default=True,
        ),
    ]
