
from rest_framework.permissions import (
    BasePermission, SAFE_METHODS
)
from rest_framework.viewsets import ModelViewSet


class MultipleSerializerModelViewSet(ModelViewSet):
    WRITE_SERIALIZER_ACTIONS = ["create", "update"]
    GET_SERIALIZER_ACTIONS = ["list", "retrieve"]

    write_serializer_class = None
    update_serializer_class = None
    create_serializer_class = None
    serializer_class = None
    list_serializer_class = None
    details_serializer_class = None
    read_serializer_class = None

    def __get_proper_write_serializer_class(self):
        serializer_class = None
        action = self.action

        if action == "create":
            serializer_class = self.create_serializer_class
        elif action == "update":
            serializer_class = self.update_serializer_class

        if not serializer_class:
            serializer_class = self.write_serializer_class

        return serializer_class

    def __get_proper_get_serializer_class(self):
        serializer_class = None
        action = self.action

        if action == "list":
            serializer_class = self.list_serializer_class
        elif action == "retrieve":
            serializer_class = self.details_serializer_class

        if not serializer_class:
            serializer_class = self.read_serializer_class

        return serializer_class

    def get_serializer_class(self):
        serializer_class = None

        if self.request.method in SAFE_METHODS:
            serializer_class = self.__get_proper_get_serializer_class()
        else:
            serializer_class = self.__get_proper_write_serializer_class()

        return serializer_class or self.serializer_class


class BaseAccessRestrictedMixin(object):
    pass
