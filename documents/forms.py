from django import forms

from .models import BaseDocument, Document, DocumentName, Provider


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["name", "number", "date",
                  "base", "provider"]
