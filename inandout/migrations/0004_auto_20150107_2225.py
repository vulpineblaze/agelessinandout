# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('inandout', '0003_auto_20150107_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageobjecthtml',
            name='content',
            field=tinymce.models.HTMLField(default=b'delete this to add text.', max_length=4000, verbose_name=b'This will override all other Page Object components!'),
            preserve_default=True,
        ),
    ]
