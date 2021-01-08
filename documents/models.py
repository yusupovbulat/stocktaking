from django.db import models


class DocumentName(models.Model):
    name = models.CharField(
        max_length=115,
        blank=False,
        null=False,
        unique=True
    )

    class Meta:
        db_table = "document_name"
