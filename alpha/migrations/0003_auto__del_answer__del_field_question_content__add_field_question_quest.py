# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Answer'
        db.delete_table('alpha_answer')

        # Deleting field 'Question.content'
        db.delete_column('alpha_question', 'content')

        # Adding field 'Question.question'
        db.add_column('alpha_question', 'question',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Question.answer'
        db.add_column('alpha_question', 'answer',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Answer'
        db.create_table('alpha_answer', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alpha.Question'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('alpha', ['Answer'])

        # Adding field 'Question.content'
        db.add_column('alpha_question', 'content',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)

        # Deleting field 'Question.question'
        db.delete_column('alpha_question', 'question')

        # Deleting field 'Question.answer'
        db.delete_column('alpha_question', 'answer')


    models = {
        'alpha.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
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