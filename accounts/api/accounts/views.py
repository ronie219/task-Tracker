from rest_framework.generics import CreateAPIView

from .serializer import accountCreation

class accountCreationAPI(CreateAPIView):
    serializer_class = accountCreation
    permission_classes = []
    authentication_classes = []
