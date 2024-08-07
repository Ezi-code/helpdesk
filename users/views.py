from rest_framework import status
from rest_framework.response import Response
from .serializer import UserSerializer, User
from rest_framework.views import APIView


class UserView(APIView):
    serializer = UserSerializer

    def get(self, request, pk=None):
        if pk:
            data = User.objects.get(pk=pk)
            serlalizer = self.serializer(data)
            return Response(serlalizer.data)
        data = User.objects.all()
        serializer = self.serializer(data)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk=None):
        if pk:
            data = User.objects.get(pk=pk)
            serializer = self.serializer(data, data=request.data, partial=True)
            serializer.is_valid(raise_excerption=True)
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        obj = User.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
