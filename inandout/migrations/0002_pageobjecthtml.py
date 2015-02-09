# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('inandout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageObjectHTML',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', tinymce.models.HTMLField(default=b'delete this to add text.', max_length=400, verbose_name=b'Text to appear in this object.')),
                ('parent', models.ForeignKey(related_name='htmls', verbose_name=b'Which PageObject does this belong to?', to='inandout.PageObject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
