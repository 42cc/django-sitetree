# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sitetree.models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetree', '0004_auto__add_field_tree_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='treeitem',
            name='access_guest',
            field=models.BooleanField(default=False, help_text='Check it to grant access to this item to guests only.', db_index=True, verbose_name='Guests only'),
            preserve_default=False,
        )
    ]
