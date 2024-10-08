from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True , editable= False ,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

       # By setting abstract = True, you're indicating that this class is not meant to be used directly, but rather as a base class for other classes to inherit from. This is useful when you want to define a common interface or set of methods that should be implemented by its subclasses.