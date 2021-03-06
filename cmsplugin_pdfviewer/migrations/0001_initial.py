# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.conf import settings


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PDFViewer'
        pdfviewer_fields = (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        )

        if getattr(settings, 'PDFVIEWER_USE_FILER', False):
            pdfviewer_fields += (('pdf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.File'])),)
        else:
            pdfviewer_fields += (('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100)),)

        db.create_table(u'cmsplugin_pdfviewer_pdfviewer', pdfviewer_fields)
        db.send_create_signal(u'cmsplugin_pdfviewer', ['PDFViewer'])


    def backwards(self, orm):
        # Deleting model 'PDFViewer'
        db.delete_table(u'cmsplugin_pdfviewer_pdfviewer')

    if getattr(settings, 'PDFVIEWER_USE_FILER', False):
        models = {
            u'auth.group': {
                'Meta': {'object_name': 'Group'},
                u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
                'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
            },
            u'auth.permission': {
                'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
                'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
                'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
                u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
            },
            u'auth.user': {
                'Meta': {'object_name': 'User'},
                'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
                'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
                'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
                'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
                u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
                'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
                'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
                'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
                'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
                'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
                'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
                'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
            },
            'cms.cmsplugin': {
                'Meta': {'object_name': 'CMSPlugin'},
                'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
                'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
                u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
                'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
                'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
                'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
                'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
                'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
            },
            'cms.placeholder': {
                'Meta': {'object_name': 'Placeholder'},
                'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
                u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
            },
            u'cmsplugin_pdfviewer.pdfviewer': {
                'Meta': {'object_name': 'PDFViewer', '_ormbases': ['cms.CMSPlugin']},
                u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
                'pdf': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.File']"}),
                'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
            },
            u'contenttypes.contenttype': {
                'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
                'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
                u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
                'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
            },
            'filer.file': {
                'Meta': {'object_name': 'File'},
                '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
                'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
                'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
                'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
                'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
                u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
                'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
                'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
                'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
                'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': u"orm['auth.User']"}),
                'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
                'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
                'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
            },
            'filer.folder': {
                'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
                'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
                u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
                'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
                'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
                'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
                u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
            }
        }
    else:
        models = {
            'cms.cmsplugin': {
                'Meta': {'object_name': 'CMSPlugin'},
                'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
                'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
                u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
                'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
                'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
                'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
                'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
                'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
            },
            'cms.placeholder': {
                'Meta': {'object_name': 'Placeholder'},
                'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
                u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
            },
            u'cmsplugin_pdfviewer.pdfviewer': {
                'Meta': {'object_name': 'PDFViewer', '_ormbases': ['cms.CMSPlugin']},
                u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
                'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
                'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
            }
        }

    complete_apps = ['cmsplugin_pdfviewer']