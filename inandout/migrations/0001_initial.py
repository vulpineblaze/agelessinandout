# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import tinymce.models
import oauth2client.django_orm


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_title', models.CharField(default=b'default CMS title.', max_length=80, verbose_name=b'Title to be shown on Browser.')),
                ('disclaimer_text', models.CharField(default=b'default disclaimer text.', max_length=2000, verbose_name=b'Disclaimer Text to show on all pages.')),
                ('disclaimer_background_color', models.CharField(default=b'#555', max_length=20, verbose_name=b'Disclaimer Background Color. Use HTML acceptable names or Hex Code.')),
                ('disclaimer_text_color', models.CharField(default=b'#ccc', max_length=20, verbose_name=b'Disclaimer Text Color. Use HTML acceptable names or Hex Code.')),
                ('background_image', models.ImageField(default=b'None/no-img.png', upload_to=b'basepage_folder/', verbose_name=b'Image for the Background.')),
                ('banner_image', models.ImageField(default=b'None/no-img.png', upload_to=b'basepage_folder/', verbose_name=b'Top of page Banner Image.')),
                ('link_hover_color', models.CharField(default=b'orange', max_length=60, verbose_name=b'Link Hover Color. Use HTML acceptable names or Hex Code.')),
                ('menu_bar_color', models.CharField(default=b'#1d5065', max_length=60, verbose_name=b'Menu Bar Color. Use HTML acceptable names or Hex Code.')),
                ('menu_accent_color', models.CharField(default=b'#3d7085', max_length=60, verbose_name=b'Menu Accent Color. Use HTML acceptable names or Hex Code.')),
                ('menu_background_color', models.CharField(default=b'#ccc', max_length=60, verbose_name=b'Menu Background Color. Use HTML acceptable names or Hex Code.')),
                ('site_name', models.CharField(default=b'', max_length=80, verbose_name=b'Facebook API - site name.')),
                ('site_desc', models.CharField(default=b'', max_length=200, verbose_name=b'Facebook API - site description default value.')),
                ('fb_app_id', models.CharField(default=b'', max_length=200, verbose_name=b'Facebook API - App ID.')),
                ('fb_page_link', models.CharField(default=b'', max_length=200, verbose_name=b'Facebook API - Link to company Facebook Page.')),
            ],
            options={
                'verbose_name_plural': 'BasePage',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=False, verbose_name=b'If unchecked, Blog will not display on website')),
                ('created', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
                ('frontpage', models.BooleanField(default=False, verbose_name=b'If Checked, Blog will display on Front Page')),
                ('priority', models.IntegerField(default=1, verbose_name=b'Determines Priorty on the Front Page. Higher numbers show higher on the Front Page.')),
                ('title', models.CharField(max_length=80, verbose_name=b"Blog's title")),
                ('preview_text', models.CharField(max_length=160, verbose_name=b'Short preview shown in Blog list page')),
                ('html_text', tinymce.models.HTMLField(max_length=4000, verbose_name=b'The main text of the Blog')),
                ('author', models.CharField(default=b' ', max_length=200, verbose_name=b"Author's visible name.")),
                ('fb_author_link', models.CharField(default=b' ', max_length=200, verbose_name=b"Facebook API - Link to Author's Facebook Page.")),
                ('main_image', models.ImageField(default=b'None/no-img.png', upload_to=b'blog_folder/', verbose_name=b'Image for the blog. Should be a wide rectangle, if possible')),
                ('preview_image', models.ImageField(default=b'None/no-img.png', upload_to=b'blog_folder/', verbose_name=b'Preview Image shown on the Index page.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=False, verbose_name=b'If unchecked, Brand will not display on website')),
                ('created', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
                ('priority', models.IntegerField(default=1, verbose_name=b'Determines Priorty. Higher numbers show higher in list.')),
                ('short_name', models.CharField(max_length=80, verbose_name=b'Brand Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('credential', oauth2client.django_orm.CredentialsField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FrontPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_text', models.CharField(default=b'This is the default frontpage main text', max_length=4000, verbose_name=b'Main text for the front page (aka Home)')),
            ],
            options={
                'verbose_name_plural': 'FrontPage',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=False, verbose_name=b'If unchecked, Object will not display on website')),
                ('page', models.CharField(default=b'FP', max_length=2, verbose_name=b'Which Page should this object display on?', choices=[(b'FP', b'Front Page (Home)'), (b'AU', b'About Us'), (b'CT', b'Contact')])),
                ('width', models.IntegerField(default=420, verbose_name=b'Set Size (Width) for Object. Be sure that complementary objects exist to prevent issues!', choices=[(270, b'Thirds'), (420, b'Half'), (880, b'Full')])),
                ('title', models.CharField(default=b'delete this to add title.', max_length=80, verbose_name=b'Title to appear on admin page.')),
                ('priority', models.IntegerField(default=0, verbose_name=b'Higher numbers show higher on the page.')),
                ('created', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageObjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'', verbose_name=b'Image to appear in this object.')),
                ('parent', models.ForeignKey(related_name='images', verbose_name=b'Which PageObject does this belong to?', to='inandout.PageObject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageObjectLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_youtube', models.BooleanField(default=False, verbose_name=b'Check this if link is a youtube video!')),
                ('link', models.URLField(default=b'', max_length=300, verbose_name=b'Link to appear in this object.')),
                ('parent', models.ForeignKey(related_name='links', verbose_name=b'Which PageObject does this belong to?', to='inandout.PageObject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageObjectText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(default=b'delete this to add text.', max_length=400, verbose_name=b'Text to appear in this object.')),
                ('parent', models.ForeignKey(related_name='texts', verbose_name=b'Which PageObject does this belong to?', to='inandout.PageObject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=False, verbose_name=b'If unchecked, Product will not display on website')),
                ('frontpage', models.BooleanField(default=False, verbose_name=b'If Checked, Product will display on Front Page')),
                ('priority', models.IntegerField(default=1, verbose_name=b'Determines Priorty on the Front Page. Higher numbers show higher on the Front Page.')),
                ('created', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
                ('short_name', models.CharField(max_length=80, verbose_name=b'Short field used on Product List page')),
                ('long_name', models.CharField(max_length=200, verbose_name=b'Longer name used in Product detail apge')),
                ('long_text', models.CharField(max_length=2000, verbose_name=b'A long description of the product, paragraphs OK')),
                ('amazon_link', models.URLField(default=b'', max_length=300, verbose_name=b'Amazon link to the Products purchase page')),
                ('main_image', models.ImageField(default=b'None/no-img.png', upload_to=b'product_folder/', verbose_name=b"Image for the product. Should be as 'square' as possible")),
                ('background_image', models.ImageField(default=b'None/no-back-img.png', upload_to=b'product_folder/', verbose_name=b'Background image fr product display.')),
                ('background_and_text_color', models.CharField(default=b'green', max_length=20, verbose_name=b'Background and Text Color. Use HTML acceptable names or Hex Code.')),
                ('brand', models.ForeignKey(related_name='brand', verbose_name=b'Which Brand does this belong to?', blank=True, to='inandout.Brand', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Testamonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=False, verbose_name=b'If unchecked, Testamonial will not display on website')),
                ('created', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
                ('frontpage', models.BooleanField(default=False, verbose_name=b'If Checked, Testamonial will display on Front Page')),
                ('priority', models.IntegerField(default=1, verbose_name=b'Determines Priorty on the Front Page. Higher numbers show higher on the Front Page.')),
                ('email_address', models.EmailField(max_length=75, verbose_name=b'Email address of submitter', blank=True)),
                ('text', models.CharField(max_length=400, verbose_name=b'Testamonial text')),
                ('nickname', models.CharField(max_length=80, verbose_name=b'Nickname of submitter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
