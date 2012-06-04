# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table('alpha_subject')


        # Renaming column for 'Question.subject' to match new field type.
        db.rename_column('alpha_question', 'subject_id', 'subject')
        # Changing field 'Question.subject'
        db.alter_column('alpha_question', 'subject', self.gf('django.db.models.fields.CharField')(max_length=7, null=True))
        # Removing index on 'Question', fields ['subject']
        db.delete_index('alpha_question', ['subject_id'])


    def backwards(self, orm):
        # Adding index on 'Question', fields ['subject']
        db.create_index('alpha_question', ['subject_id'])

        # Adding model 'Subject'
        db.create_table('alpha_subject', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('alpha', ['Subject'])


        # Renaming column for 'Question.subject' to match new field type.
        db.rename_column('alpha_question', 'subject', 'subject_id')
        # Changing field 'Question.subject'
        db.alter_column('alpha_question', 'subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alpha.Subject'], null=True))

    models = {
        'alpha.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True'})
        }
    }

    complete_apps = ['alpha']