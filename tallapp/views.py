from django.urls import path
from .import views
import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import  *
from django.db.models import Count
from django.contrib import messages
import datetime
import fiscalyear
from fiscalyear import *
from dateutil import relativedelta


# Create your views here.
def home(request):
    return render(request,'base.html')
def recon(request):
    return render(request,'bank_reconcilliation.html')
def load_create_ledgers(request):
    return render(request,'load_create_ledgers.html')   
def searchbank(request):
    group=groups.objects.get(group="bank account")
    

    led=ledger.objects.filter(group=group.id)
    

    return render(request,'search_bank.html',{'l':led})

def deposit(request,id):
    sum=0
    led=ledger.objects.get(id=id)
    uid=led.id
    
    v=Vouchertype.objects.all()
    for v in v:
        if v.vouchertype=='payment':
            vid=v.id


   
    bak=bank.objects.filter(~Q(vouchertype=vid)).filter(ledger=uid)
    back=bak
    for back in back:
        b=back.amount.amount
        sum=sum+b

    return render(request,'deposit_slip.html',{'bank':bak,'vi':v,'sum':sum})


def searchledger(request):
    group=groups.objects.get(group= "ledger account")
    led=ledger.objects.filter(group=group.id)
    return render(request,'search_ledger.html',{'l':led})

def payment_advice(request,id):
    sum=0
    led=ledger.objects.get(id=id)
    uid=led.id
    
    pay=payment.objects.all().filter(ledger=uid)
    # v=Vouchertype.objects.all()
    # for v in v:
    #     if v.vouchertype=='payment':
    #         vid=v.id
    
    pays=pay
    for pays in pay:
        p=pays.amount.amount
        sum=sum+p

   
    # bak=bank.objects.filter(vouchertype=vid).filter(ledger=uid)
    return render(request,'payment_advice.html',{'p':pay,'sum':sum})
def searchbank1(request):
    group=groups.objects.get(group="bank account")
    

    led=ledger.objects.filter(group=group.id)
    
    return render(request,'banksearch.html',{'l':led})



def reconciliation(request,id):
    bak=bank.objects.filter(id=id)
    b=bank.objects.all()
    # par=Particulars.objects.get(particualrs=id)
    credit={}
    debit={}
    con=contra.objects.all()
    pay=payment.objects.all()
    rec=receipt.objects.all()
    cont=bank.objects.filter(vouchertype_id=1)
    print('hi')
    print(cont)
    print('hi')
    led=ledger.objects.get(id=id)
    
    print(bak)
    print(led)
    for b in b:
        if b.ledger.id==led.id:
            print(b.ledger.id)
            print(led.id)
            credit[b.id]=b.amount.amount
        else:
            if b.amount.particualrs==led:
                print( b.amount.particualrs)
                print(led)
                debit[b.id]=b.amount.amount
    print(credit)
    print(debit)

    # print(bak.ledger.id)
    print(led.id)

    return render(request,'bank_reconcilliation.html',{'c':con,'p':pay,'r':rec,'b':b,'l':led,'cr':credit,'de':debit})

def collection(request):
    collect=contra.objects.filter()
    return render(request,'bank_reconcilliation.html',{'c':collect})



#     check_payment = payment.objects.all()
#     context={'pay':check_payment}
#     return render(request,'bank_reconcilliation.html',context)
# def reconciliation1(request):
#     check_contra=contra.objects.all()
#     context={'contra':check_contra}
#     return render(request,'bank_reconcilliation.html',context)
# def reconciliation3(request):
#     check_sales=sales.objects.all()
#     context={'sales':check_sales}
#     return render(request,'bank_reconcilliation.html',context)
# def reconciliation4(request):
#     check_journal=journal.objects.all()
#     context={'journal':check_journal}
#     return render(request,'bank_reconcilliation.html',context)
# def reconciliation5(request):
#     check_receipt=receipt.objects.all()
#     context={'sales':check_receipt}
#     return render(request,'bank_reconcilliation.html',context)







