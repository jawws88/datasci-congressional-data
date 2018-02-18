from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import viewsets

from api.models import CandidateContributions
from api.serializers import CandidateContributionSerializer


class CandidateContributionsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CandidateContributionSerializer

    # override the default query set to limit to 100 objects
    queryset = CandidateContributions.objects.all()[0:100]


# TODO: viewsets for other models, and probably more endpoints