# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inandout', '0005_auto_20150107_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='basepage',
            name='main_border_color',
            field=models.CharField(default=b'orange', max_length=60, verbose_name=b'Main Border Color. Use HTML acceptable names or Hex Code.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basepage',
            name='main_text_color',
            field=models.CharField(default=b'orange', max_length=60, verbose_name=b'Main Text Color. Use HTML acceptable names or Hex Code.'),
            preserve_default=True,
        ),
    ]
