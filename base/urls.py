
from django.urls import path
from . import views

# simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.endPoints, name='endPoints'),
    path('advocates/', views.AdvocatesList.as_view(), name='advocate_list'),

    path('advocates/<str:username>/',
         views.AdvocateDetail.as_view(), name='advocate_detail'),

    path('company/', views.CompanyList.as_view(), name='company_list'),

    # simple jwt routes
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

# company endpoint
# company/
# company/:name
