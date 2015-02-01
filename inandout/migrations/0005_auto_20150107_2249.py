# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inandout', '0004_auto_20150107_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageobject',
            name='width',
            field=models.IntegerField(default=420, verbose_name=b'Set Size (Width) for Object. Be sure that complementary objects exist to prevent issues!', choices=[(270, b'Thirds'), (420, b'Half'), (870, b'Full')]),
            preserve_default=True,
        ),
    ]
