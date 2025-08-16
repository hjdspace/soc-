from rest_framework import viewsets
from .models import Project, Release, TestPlan, TestCase, Bug
from .serializers import (
    ProjectSerializer,
    ReleaseSerializer,
    TestPlanSerializer,
    TestCaseSerializer,
    BugSerializer
)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

class TestPlanViewSet(viewsets.ModelViewSet):
    queryset = TestPlan.objects.all()
    serializer_class = TestPlanSerializer

class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer

class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
