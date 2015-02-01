# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('inandout', '0002_pageobjecthtml'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageobjecthtml',
            name='content',
            field=tinymce.models.HTMLField(default=b'delete this to add text.', max_length=400, verbose_name=b'This will override all other Page Object components!'),
            preserve_default=True,
        ),
    ]
