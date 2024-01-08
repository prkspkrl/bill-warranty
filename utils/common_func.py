# import time

# def generate_invoice_number():
#     timestamp = int(time.time())
#     invoice_number = f'WN-{timestamp}'
#     return invoice_number


import time

class InvoiceGenerator:
    def __init__(self, prefix='WN'):
        self.prefix = prefix

    def generate_invoice_number(self):
        timestamp = int(time.time())
        invoice_number = f'{self.prefix}-{timestamp}'
        return invoice_number