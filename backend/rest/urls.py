from django.urls import path
from .views import addReport, projects, reports
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)


urlpatterns = [
    path('projects/', projects.as_view(), name="Projects"),
    path('add-report/', addReport.as_view(), name="Add-Report"),
    path('reports/', reports.as_view(), name="Reports"),
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),




















    
    # path('protegida/', Protegida.as_view(), name='protegida'),
    # path('', LoginAPIView.as_view(), name='login'),
    # path('verify-token/', TokenVerifyView.as_view(), name='token_verify'),


]


