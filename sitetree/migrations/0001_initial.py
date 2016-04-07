# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sitetree.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.CharField(help_text='Short name to address site tree from templates.<br /><b>Note:</b> change with care.', unique=True, max_length=80, verbose_name='Alias', db_index=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Site Tree',
                'verbose_name_plural': 'Site Trees',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TreeItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Site tree item title. Can contain template variables E.g.: {{ mytitle }}.', max_length=100, verbose_name='Title')),
                ('hint', models.CharField(default='', help_text='Some additional information about this item that is used as a hint.', max_length=200, verbose_name='Hint', blank=True)),
                ('url', models.CharField(help_text='Exact URL or URL pattern (see "Additional settings") for this item.', max_length=200, verbose_name='URL', db_index=True)),
                ('urlaspattern', models.BooleanField(default=False, help_text='Whether the given URL should be treated as a pattern.<br /><b>Note:</b> Refer to Django "URL dispatcher" documentation (e.g. "Naming URL patterns" part).', db_index=True, verbose_name='URL as Pattern')),
                ('hidden', models.BooleanField(default=False, help_text='Whether to show this item in navigation.', db_index=True, verbose_name='Hidden')),
                ('alias', sitetree.models.CharFieldNullable(max_length=80, blank=True, help_text='Short name to address site tree item from a template.<br /><b>Reserved aliases:</b> "trunk", "this-children", "this-siblings", "this-ancestor-children", "this-parent-siblings".', null=True, verbose_name='Alias', db_index=True)),
                ('description', models.TextField(default='', help_text='Additional comments on this item.', verbose_name='Description', blank=True)),
                ('inmenu', models.BooleanField(default=True, help_text='Whether to show this item in a menu.', db_index=True, verbose_name='Show in menu')),
                ('inbreadcrumbs', models.BooleanField(default=True, help_text='Whether to show this item in a breadcrumb path.', db_index=True, verbose_name='Show in breadcrumb path')),
                ('insitetree', models.BooleanField(default=True, help_text='Whether to show this item in a site tree.', db_index=True, verbose_name='Show in site tree')),
                ('sort_order', models.IntegerField(default=0, help_text='Item position among other site tree items under the same parent.', verbose_name='Sort order', db_index=True)),
                ('access_permissions', models.ManyToManyField(to='auth.Permission', verbose_name='Permissions granting access', blank=True)),
                ('parent', models.ForeignKey(related_name='treeitem_parent', blank=True, to='sitetree.TreeItem', help_text='Parent site tree item.', null=True, verbose_name='Parent')),
                ('tree', models.ForeignKey(related_name='treeitem_tree', verbose_name='Site Tree', to='sitetree.Tree', help_text='Site tree this item belongs to.')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Site Tree Item',
                'verbose_name_plural': 'Site Tree Items',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='treeitem',
            unique_together=set([('tree', 'alias')]),
        ),
    ]
