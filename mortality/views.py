from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Cause
from .serializers import CauseSerializer


class CauseViewSet(viewsets.ViewSet):
    queryset = Cause.objects.all()

    def list(self, request):
        queryset = Cause.objects.all()
        serializer = CauseSerializer(queryset, many=True)
        return Response(serializer.data)
