# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Product')),
            ],
            options={
                'db_table': 'featured_products',
            },
        ),
    ]
