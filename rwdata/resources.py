from import_export import resources
from .models import CataxDB

class CataxDBResource(resources.ModelResource):
    class meta:
        model = CataxDB