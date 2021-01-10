from django.shortcuts import render
from django.urls import reverse

from .models import Document
from .forms import DocumentForm


def index(request):
    documents = Document.objects.all()
    return render(request, "documents/index.html", {
        "documents": documents
    })


def add(request):
    form = DocumentForm()
    return render(request, "documents/add.html", {
        "form": form
    })
