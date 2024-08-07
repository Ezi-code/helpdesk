

from django.shortcuts import render
from .serializer import CompliantSerializer, Compliant
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CompliantView(APIView):
    serializer = CompliantSerializer

    def get(self, request, pk=None):
        if pk:
            data = Compliant.objects.get(pk=pk)
            serlalizer = self.serializer(data)
            return Response(serlalizer.data)
        data = Compliant.objects.all()
        serializer = self.serializer(data)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk=None):
        if pk:
            data = Compliant.objects.get(pk=pk)
            serializer = self.serializer(data, data=request.data, partial=True)
            serializer.is_valid(raise_excerption=True)
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        obj = Compliant.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
