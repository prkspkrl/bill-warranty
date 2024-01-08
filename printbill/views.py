from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.views import View
from .models import Bill
from datetime import datetime
from utils.common_func import *
from django.shortcuts import get_object_or_404 
import imgkit
from django.http import HttpResponse

from django.http import HttpResponse
from django.template.loader import get_template
import weasyprint

from io import BytesIO

from django.http import HttpResponse
from reportlab.pdfgen import canvas

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

class AddBillView(View):
    template_name = 'add_bill.html'

    def get(self, request):
        try:
            hi = Bill.objects.all()
            return render(request, self.template_name)

        except Exception as e:
            raise e

    def post(self, request, price=None, quantity=None):
        invoice_generator = InvoiceGenerator(prefix='INV')

        try:

            if request.method == 'POST':
                customer_name = request.POST.get('customer_name')
                address = request.POST.get('address')
                phone_number = request.POST.get('phone_number')
                watch_name = request.POST.get('watch_model')
                invoice = invoice_generator.generate_invoice_number()
                price = request.POST.get('price')
                # price = price is not None request.POST.get('price') else 0

                quantity = request.POST.get('quantity')
                payment_method = request.POST.get('payment_method')
                note = request.POST.get('note')

                subtotal = int(price) *int(quantity)
                grand_total = int(subtotal) + int(100)

                print(request.POST)

                bill = Bill.objects.create(
                    customer_name = customer_name,
                    address=address,
                    phone_number=phone_number,
                    watch_name = watch_name,
                    invoice=invoice,
                    price = price,
                    quantity=quantity,
                    payment_method = payment_method,
                    subtotal = subtotal,
                    grand_total = grand_total,
                    note = note,
                )
                return redirect('home')
            
            else:
                print("not post")
        
        except Exception as e:
            return render(request,self.template_name)
            raise e    



class BillPage(View):
    template_name = 'bill.html'

    def get(self,request, pk):
        bill = get_object_or_404(Bill, pk=pk)
        context = {'bill': bill}

        return render(request, self.template_name, context)




class PrintBillView(View):
    template_name = 'pdf.html'

    def get(self, request, pk):
        try:
            bill = get_object_or_404(Bill, pk=pk)
            context = {'bill': bill}

            # Render the template to HTML
            template = get_template(self.template_name)
            html = template.render(context)

            # Create a PDF file using WeasyPrint
            pdf_file = weasyprint.HTML(string=html).write_pdf()

            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{bill.invoice}.pdf"'

            return response

        except BaseException as e:
            raise e


class GenerateImage(View):

    template_name ='templates/bill.html'

    def get(self, request):
        with open(self.template_name, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Specify the options for imgkit
        options = {
            'format': 'jpg',
            'width': '800',  # Adjust the width as needed
            # 'path' : '/usr/bin/wkhtmltoimage'

        }
        image = imgkit.from_string(html_content, False, options=options)
        response = HttpResponse(image, content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="invoice.jpg"'

        return response


