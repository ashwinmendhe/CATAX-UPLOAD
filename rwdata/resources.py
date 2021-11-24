from import_export import resources
from .models import CataxDBnew

class CataxDBnewResource(resources.ModelResource):
    class meta:
        model = CataxDBnew