# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'item'
        db.create_table('ecommerce_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('product_page', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('ecommerce', ['item'])

        # Adding model 'similarItems'
        db.create_table('ecommerce_similaritems', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ecommerce', ['similarItems'])

    def backwards(self, orm):
        # Deleting model 'item'
        db.delete_table('ecommerce_item')

        # Deleting model 'similarItems'
        db.delete_table('ecommerce_similaritems')

    models = {
        'ecommerce.item': {
            'Meta': {'object_name': 'item'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'product_page': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'ecommerce.similaritems': {
            'Meta': {'object_name': 'similarItems'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['ecommerce']