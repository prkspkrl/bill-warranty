from django.shortcuts import render
from django.views import View
from .models import WarrantyCard
from django.shortcuts import get_object_or_404
from printbill.models import Bill
from django.template.loader import get_template
import weasyprint
from django.http import HttpResponse


class WarrantyListView(View):
    template_name = 'warranty.html'
    def get(self, request, pk):
        try:
            warranty_list = Bill.objects.filter(pk=pk)
            for i in warranty_list:
                context ={
                    'i': i,
                }

        except Exception as e:
            raise e

        return render(request, self.template_name, context)

    def post(self, request, pk):
        pass


class WarrantyPdfView(View):
    template_name ="warranty_pdf.html"

    def get(self, request, pk):
        try:
            bill = get_object_or_404(Bill, pk=pk)
            print(bill.customer_name)
            print(bill.address)
            context = {'bill': bill}

            template = get_template(self.template_name)
            html = template.render(context)

            # Create a PDF file using WeasyPrint
            pdf_file = weasyprint.HTML(string=html).write_pdf()

            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{bill.invoice}.pdf"'

            return response

        except BaseException as e:
            raise e
