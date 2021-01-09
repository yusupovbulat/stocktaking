from django.db import models
from datetime import date


def today_date():
    return date.today().strftime("YYYY-MM-DD")


class DocumentName(models.Model):
    """
    Contains document names
    """
    name = models.CharField(
        max_length=115,
        blank=False,
        null=False,
        unique=True
    )

    class Meta:
        db_table = "document_name"

    def __str__(self):
        return f"{self.name}"


class Provider(models.Model):
    """
    Contains providers
    """
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "provider"

    def __str__(self):
        return f"{self.name}"


class Document(models.Model):
    """
    Contains documents
    """
    name = models.ForeignKey(
        DocumentName,
        on_delete=models.CASCADE,
        related_name="documents",
    )
    number = models.CharField(
        max_length=20,
        null=False,
        blank=True,
    )
    date = models.DateField(default=today_date())
    base_number = models.CharField(max_length=20, blank=True)
    base_date = models.DateField(default=today_date())
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    class Meta:
        db_table = "document"

    def __str__(self):
        return f"{self.name} №{self.number} от {self.date}"
