from rest_framework import viewsets

from api.models import CandidateContributions
from api.serializers import CandidateContributionSerializer


class CandidateContributionsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CandidateContributionSerializer

    # override the default query set to limit to 100 objects, just for this sample app
    queryset = CandidateContributions.objects.all()[0:100]


# more ViewSets or views would go here, depending on what data we need to power the visualization