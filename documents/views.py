from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Document, BaseDocument
from .forms import BaseDocumentForm, DocumentForm


def index(request):
    documents = Document.objects.all()
    return render(request, "documents/index.html", {
        "documents": documents
    })


def document_create(request):
    form = DocumentForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponseRedirect("/")
    return render(request, "document_form.html", {
        "form": form
    })


def base_document_create_popup(request):
    form = BaseDocumentForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse("<script>opener.closePopup(window, '%s', '%s', '#id_base');</script>" % (instance.pk, instance))
    return render(request, "base_document_form.html", {
        "form": form
    })


def base_document_edit_popup(request):
    instance = get_object_or_404(BaseDocument, pk=pk)
    form = BaseDocumentForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save()
        return HttpResponse("<script>opener.closePopup(window, '%s', '%s', '#id_base');</script>" % (instance.pk, instance))
    return render(request, "base_document_form.html", {
        "form": form
    })


@csrf_exempt
def get_base_id(request):
    if request.is_ajax():
        base_number = request.GET['number']
        base_id = BaseDocument.objects.get(number=base_number).id
        data = {"base_id": base_id}
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse("/")
