# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Question.answer'
        db.alter_column('alpha_question', 'answer', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Question.question'
        db.alter_column('alpha_question', 'question', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Question.subject'
        db.alter_column('alpha_question', 'subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alpha.Subject'], null=True))

    def backwards(self, orm):

        # Changing field 'Question.answer'
        db.alter_column('alpha_question', 'answer', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Question.question'
        db.alter_column('alpha_question', 'question', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Question.subject'
        db.alter_column('alpha_question', 'subject_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['alpha.Subject']))

    models = {
        'alpha.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alpha.Subject']", 'null': 'True'})
        },
        'alpha.subject': {
            'Meta': {'object_name': 'Subject'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['alpha']