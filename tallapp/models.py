from django.db import models

#Create your models here.
class Vouchertype(models.Model):
    vouchertype=models.CharField(max_length=255,null=True)

class groups(models.Model):
    group=models.CharField(max_length=225)


    def __str__(self):
     return self.group

class ledger(models.Model):
    group=models.ForeignKey(groups,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=225)
    
    def __str__(self):
     return self.name

class transactiontype(models.Model):
    transactiontype=models.CharField(max_length=225)


class account(models.Model):
     
     account=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
     date=models.DateTimeField()

class Particulars(models.Model):
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
    amount=models.IntegerField()


class contra(models.Model):
    ledger=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
    vouchertype=models.ForeignKey(Vouchertype,on_delete=models.CASCADE,null=True)
    no=models.IntegerField()   
    date=models.ForeignKey(account,on_delete=models.CASCADE,null=True)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)

class payment(models.Model):
    ledger=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)
    vouchertype=models.ForeignKey(Vouchertype,on_delete=models.CASCADE,null=True)
    no=models.IntegerField()   
    date=models.ForeignKey(account,on_delete=models.CASCADE,null=True)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)

class bank(models.Model):
    ledger=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
    transactiontype=models.ForeignKey(transactiontype,on_delete=models.CASCADE,null=True)
    instno=models.IntegerField()
    instdate=models.DateField()
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    date=models.ForeignKey(account,on_delete=models.CASCADE,null=True)
    vouchertype=models.ForeignKey(Vouchertype,on_delete=models.CASCADE,null=True)
   
class receipt(models.Model):
    no=models.IntegerField()   
    date=models.ForeignKey(account,on_delete=models.CASCADE,null=True)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    vouchertype=models.ForeignKey(Vouchertype,on_delete=models.CASCADE,null=True)

class sales(models.Model):
    no=models.IntegerField()   
    date=models.ForeignKey(account,on_delete=models.CASCADE,null=True)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    vouchertype=models.ForeignKey(Vouchertype,on_delete=models.CASCADE,null=True)
class journal(models.Model):
    no=models.IntegerField()   
    date=models.ForeignKey(account,on_delete=models.CASCADE,null=True)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    vouchertype=models.ForeignKey(Vouchertype,on_delete=models.CASCADE,null=True)
    






