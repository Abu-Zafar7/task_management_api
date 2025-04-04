
from django.urls import path, include
from rest_framework import routers
from tasks.views import TaskViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]

