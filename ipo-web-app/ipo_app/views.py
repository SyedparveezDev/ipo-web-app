from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IPO
from .serializers import IPOSerializer

class IPOListAPIView(APIView):
    def get(self, request):
        ipos = IPO.objects.all()
        serializer = IPOSerializer(ipos, many=True)
        return Response(serializer.data)

class IPODetailAPIView(APIView):
    def get(self, request, pk):
        try:
            ipo = IPO.objects.get(pk=pk)
            serializer = IPOSerializer(ipo)
            return Response(serializer.data)
        except IPO.DoesNotExist:
            return Response({"error": "IPO not found"}, status=status.HTTP_404_NOT_FOUND)

