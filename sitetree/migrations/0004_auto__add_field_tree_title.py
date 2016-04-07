# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sitetree.models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetree', '0003_auto__add_field_treeitem_access_loggedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='title',
            field=models.CharField(help_text='Site tree title for presentational purposes.', max_length=100, verbose_name='Title', blank=True),
            preserve_default=False,
        )
    ]
