# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roofy', '0005_client_main_contact_last_name'),
    ]

    operations = [
    migrations.RenameModel('SiteInformation', 'Projects')
    ]
