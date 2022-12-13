from django.urls import path,include
from rest_framework import routers 
from .views import MemberViewSet 
router=routers.DefaultRouter() 
router.register(r'',MemberViewSet)
urlpatterns=[
    path('',include(router.urls))
   
]