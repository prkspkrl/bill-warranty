from django.urls import path
from .views import *

app_name = 'warranty'

urlpatterns = [
    path('listcard/<str:pk>', WarrantyListView.as_view(), name='warranty'),
    path('pdf/<str:pk>', WarrantyPdfView.as_view(), name='warrantypdf'),

]