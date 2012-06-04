# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table('alpha_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alpha.Subject'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('alpha', ['Question'])

        # Adding model 'Subject'
        db.create_table('alpha_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('alpha', ['Subject'])

        # Adding model 'Answer'
        db.create_table('alpha_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alpha.Question'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('alpha', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table('alpha_question')

        # Deleting model 'Subject'
        db.delete_table('alpha_subject')

        # Deleting model 'Answer'
        db.delete_table('alpha_answer')


    models = {
        'alpha.answer': {
            'Meta': {'object_name': 'Answer'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alpha.Question']"})
        },
        'alpha.question': {
            'Meta': {'object_name': 'Question'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alpha.Subject']"})
        },
        'alpha.subject': {
            'Meta': {'object_name': 'Subject'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['alpha']