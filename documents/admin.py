from django.contrib import admin

from .models import BaseDocument, Document, DocumentName, Provider

# Register your models here.
admin.site.register(Document)
admin.site.register(DocumentName)
admin.site.register(Provider)
admin.site.register(BaseDocument)
