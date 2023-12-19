import uuid
from django.db import models


class AbstractModel(models.Model):
    public_id = models.UUIDField(
        primary_key=True, db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True