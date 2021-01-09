from django.shortcuts import render
from django.urls import reverse

from .models import Document


def index(request):
    documents = Document.objects.all()
    return render(request, "documents/index.html", {
        "documents": documents
    })
