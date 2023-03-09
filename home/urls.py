from django.urls import path,include
from home.views import EmpViewSet
from rest_framework import routers





routers=routers.DefaultRouter()
routers.register(r'Emp',EmpViewSet,)






urlpatterns = [
    path('',include(routers.urls))
]