# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table('inf1820_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')(null=True)),
            ('answer', self.gf('django.db.models.fields.TextField')(null=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('inf1820', ['Question'])

        # Adding model 'Tag'
        db.create_table('inf1820_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('inf1820', ['Tag'])

        # Adding M2M table for field targets on 'Tag'
        db.create_table('inf1820_tag_targets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm['inf1820.tag'], null=False)),
            ('question', models.ForeignKey(orm['inf1820.question'], null=False))
        ))
        db.create_unique('inf1820_tag_targets', ['tag_id', 'question_id'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table('inf1820_question')

        # Deleting model 'Tag'
        db.delete_table('inf1820_tag')

        # Removing M2M table for field targets on 'Tag'
        db.delete_table('inf1820_tag_targets')


    models = {
        'inf1820.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'inf1820.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'targets': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['inf1820.Question']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['inf1820']