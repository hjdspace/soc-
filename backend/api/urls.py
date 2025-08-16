from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet,
    ReleaseViewSet,
    TestPlanViewSet,
    TestCaseViewSet,
    BugViewSet
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'releases', ReleaseViewSet)
router.register(r'testplans', TestPlanViewSet)
router.register(r'testcases', TestCaseViewSet)
router.register(r'bugs', BugViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
