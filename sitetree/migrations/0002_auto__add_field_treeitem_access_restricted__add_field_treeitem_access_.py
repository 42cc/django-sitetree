# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sitetree.models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treeitem',
            name='access_restricted',
            field=models.BooleanField(default=False, help_text='Check it to restrict user access to this item, using Django permissions system.', db_index=True, verbose_name='Restrict access to permissions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeitem',
            name='access_perm_type',
            field=models.IntegerField(default=1, help_text='<b>Any</b> &mdash; user should have any of chosen permissions. <b>All</b> &mdash; user should have all chosen permissions.', verbose_name='Permissions interpretation', choices=[(1, 'Any'), (2, 'All')]),
            preserve_default=False,
        ),
    ]
