# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Question.subject'
        db.delete_column('alpha_question', 'subject')


    def backwards(self, orm):
        # Adding field 'Question.subject'
        db.add_column('alpha_question', 'subject',
                      self.gf('django.db.models.fields.CharField')(max_length=8, null=True),
                      keep_default=False)


    models = {
        'alpha.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['alpha']