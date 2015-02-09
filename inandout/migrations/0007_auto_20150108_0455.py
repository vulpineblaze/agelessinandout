# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('inandout', '0006_auto_20150108_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageobjecthtml',
            name='content',
            field=tinymce.models.HTMLField(default=b'', max_length=4000, verbose_name=b'This will override all other Page Object components!'),
            preserve_default=True,
        ),
    ]
