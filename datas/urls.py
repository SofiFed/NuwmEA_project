from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tables', views.TableView)
router.register('customusers', views.CustomUserView)

urlpatterns = [
    path('', include(router.urls)),
]