from graphene_django.filter import DjangoFilterConnectionField

from .object_types import FileObjectType


class FilesQueries:  
    my_files = DjangoFilterConnectionField(FileObjectType)
