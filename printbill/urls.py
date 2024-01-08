from django.urls import path
from .views import *
from bill.views import *

app_name = 'printbill'

urlpatterns = [
    path('bill', AddBillView.as_view(), name='printbill'),
    path('bill/<str:pk>', BillPage.as_view(), name='printbill'),
    # path('bill/generate/', GenerateImage.as_view(), name='image-generate'),
    path('bill/delete/<str:pk>', DeleteDataView.as_view(), name='deletebill'),

    path('bill/pdf/<str:pk>/', PrintBillView.as_view(), name='print_bill_pdf'),

]