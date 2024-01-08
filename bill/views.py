from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.views import View
from printbill.models import Bill
from datetime import datetime
from utils.common_func import *

class HomeView(View):
    template_name = 'home.html'
    try:
        def get(self, request):
            list_customer = Bill.objects.all()

            context ={
                'list_customer':list_customer
            }

            return render(request, self.template_name, context)

    except Exception as e:
        raise e

class DeleteDataView(View):

    try:
        def get(self, request, pk):
            del_data = Bill.objects.get(pk=pk)
            del_data.delete()

            return redirect('home')

    except:
        print("something went worong 1")

