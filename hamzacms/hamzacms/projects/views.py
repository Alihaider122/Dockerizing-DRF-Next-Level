from rest_framework import mixins, viewsets
from .models import Projects
from .serializers import CreateProjectSerializer, ProjectSerializer


# Create your views here.
class ProjectViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    """
    Create new Project
    """
    queryset = Projects.objects.all()
    serializer_class = CreateProjectSerializer
