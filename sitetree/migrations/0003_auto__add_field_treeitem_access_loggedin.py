# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sitetree.models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetree', '0002_auto__add_field_treeitem_access_restricted__add_field_treeitem_access_'),
    ]

    operations = [
        migrations.AddField(
            model_name='treeitem',
            name='access_loggedin',
            field=models.BooleanField(default=False, help_text='Check it to grant access to this item to authenticated users only.', db_index=True, verbose_name='Logged in only'),
            preserve_default=False,
        )
    ]
