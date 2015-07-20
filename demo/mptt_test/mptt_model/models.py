from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Genre(MPTTModel):
    name = models.CharField(max_length = 50, unique=True)
    # must define
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        # indicates the natural ordering of the data in the tree
        order_insertion_by = ['name']
