from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(groups)
admin.site.register(ledger)
admin.site.register(transactiontype)
admin.site.register(account)
admin.site.register(Particulars)
admin.site.register(contra)
admin.site.register(payment)
admin.site.register(bank)
admin.site.register(sales)
admin.site.register(receipt)
admin.site.register(journal)
admin.site.register(Vouchertype)