
from django.urls import path
from . import views

urlpatterns = [
    path('',views.endPoints,name='endPoints'),
    path('advocates/',views.AdvocatesList.as_view(),name='advocate_list'),

    path('advocates/<str:username>/',views.AdvocateDetail.as_view(),name='advocate_detail'),

    path('company/',views.CompanyList.as_view(),name='company_list'),

]

# company endpoint
# company/
# company/:name
