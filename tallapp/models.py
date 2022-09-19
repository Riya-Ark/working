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
    date=models.ForeignKey(account,on_delete=models.CASCADE,null=True)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    vouchertype=models.ForeignKey(Vouchertype,on_delete=models.CASCADE,null=True)


    
# class Ledger1(models.Model):
#     ledger_name = models.CharField(max_length=225,default="Null",blank=True)
#     ledger_alias = models.CharField(max_length=225,default="Null",blank=True)
#     group_under =  models.CharField(max_length=225,default="Null",blank=True)
#     ledger_opening_bal = models.CharField(max_length=225,default="Null",blank=True)
#     ledger_type = models.CharField(max_length=225,default="Null",blank=True)
#     provide_banking_details =  models.CharField(max_length=225,default="Null",blank=True)

#     def __str__(self):
#         return self.ledger_name


# class Ledger_Banking_Details(models.Model):
#     ledger_id = models.ForeignKey(Ledger1, on_delete=models.CASCADE, null=True, blank=True)
#     od_limit = models.CharField(max_length=225,default="Null",blank=True)
#     holder_name =models.CharField(max_length=225,default="Null",blank=True)
#     ac_number =models.CharField(max_length=225,default="Null",blank=True)
#     ifsc =models.CharField(max_length=225,default="Null",blank=True)
#     swift_code =models.CharField(max_length=225,default="Null",blank=True)
#     bank_name = models.CharField(max_length=225,default="Null",blank=True)
#     branch_name = models.CharField(max_length=225,default="Null",blank=True)
#     alter_chk_bks =  models.CharField(max_length=225,default="Null",blank=True)
#     enbl_chk_printing =  models.CharField(max_length=225,default="Null",blank=True)
#     chqconfg= models.CharField(max_length=225,default="Null",blank=True)

# class Ledger_Mailing_Address(models.Model):
#     ledger_id = models.ForeignKey(Ledger1, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=225,default="Null",blank=True)
#     address = models.CharField(max_length=225,default="Null",blank=True)
#     state = models.CharField(max_length=225,default="Null",blank=True)
#     country =models.CharField(max_length=225,default="Null",blank=True)
#     pincode =models.CharField(max_length=225,default="Null",blank=True)


# class Ledger_Tax_Register(models.Model):
#     ledger_id = models.ForeignKey(Ledger1, on_delete=models.CASCADE, null=True, blank=True)
#     gst_uin = models.CharField(max_length=225,default="Null",blank=True)
#     register_type =models.CharField(max_length=225,default="Null",blank=True)
#     pan_no = models.CharField(max_length=225,default="Null",blank=True)
#     alter_gst_details = models.CharField(max_length=225,default="Null",blank=True)


# class Ledger_Satutory(models.Model):
#     ledger_id = models.ForeignKey(Ledger1, on_delete=models.CASCADE, null=True, blank=True)
#     assessable_calculation = models.CharField(max_length=225,default="Null",blank=True)
#     Appropriate_to =models.CharField(max_length=225,default="Null",blank=True)
#     gst_applicable = models.CharField(max_length=225,default="Null",blank=True)
#     Set_alter_GST =models.CharField(max_length=225,default="Null",blank=True)
#     type_of_supply = models.CharField(max_length=225,default="Null",blank=True)
#     Method_of_calc=models.CharField(max_length=225,default="Null",blank=True)

# class Ledger_Rounding(models.Model):
#     ledger_id = models.ForeignKey(Ledger1, on_delete=models.CASCADE, null=True, blank=True)
#     Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
#     Round_limit = models.CharField(max_length=22,default="Null",blank=True)

# class ledger_tax(models.Model):
#     ledger_id = models.ForeignKey(Ledger1, on_delete=models.CASCADE, null=True, blank=True)
#     type_of_duty_or_tax =models.CharField(max_length=225,default="Null",blank=True)
#     type_of_tax =models.CharField(max_length=225,default="Null",blank=True)
#     valuation_type=models.CharField(max_length=225,default="Null",blank=True)
#     rate_per_unit =models.CharField(max_length=225,default="Null",blank=True)
#     Persentage_of_calculation=models.CharField(max_length=225,default="Null",blank=True)
   

# class Ledger_sundry(models.Model):
#     ledger_id = models.ForeignKey(Ledger1, on_delete=models.CASCADE, null=True, blank=True)
#     maintain_balance_bill_by_bill =models.CharField(max_length=225,default="Null",blank=True)
#     Default_credit_period=models.CharField(max_length=225,default="Null",blank=True)
#     Check_for_credit_days=models.CharField(max_length=225,default="Null",blank=True)



class ledgercreation(models.Model):
  name=models.CharField(max_length=255,null=True)
  alias=models.CharField(max_length=255,null=True)
  under=models.CharField(max_length=255)
  bank_details=models.CharField(max_length=255,) 
  mname=models.CharField(max_length=255,null=True)
  address=models.CharField(max_length=255,null=True)
  country=models.CharField(max_length=255,null=True)
  state=models.CharField(max_length=255,null=True)
  pincode =models.IntegerField(null=True)
  pan_no =models.IntegerField(null=True)
  registration_type =models.CharField(max_length=255,null=True)
  gst_uin =models.IntegerField(null=True)
  set_alter_gstdetails =models.CharField(max_length=255,null=True)

  


  ac_holder_nm =models.CharField(max_length=255,null=True)
  acc_no =models.IntegerField(null=True) 
  ifsc_code =models.IntegerField(null=True)
  swift_code =models.IntegerField(null=True)
  bank_name =models.CharField(max_length=255,null=True) 
  branch =models.CharField(max_length=255,null=True)
  SA_cheque_bk =models.CharField(max_length=255,null=True)
  Echeque_p =models.CharField(max_length=255,null=True)

  occ_set_odl = models.CharField(max_length=255,null=True)
  occ_ac_holder_nm =models.CharField(max_length=255,null=True)
  occ_acc_no =models.IntegerField(null=True) 
  occ_ifsc_code =models.IntegerField(null=True)
  occ_swift_code =models.IntegerField(null=True)
  occ_bank_name =models.CharField(max_length=255,null=True) 
  occ_branch =models.CharField(max_length=255,null=True)
  occ_SA_cheque_bk =models.CharField(max_length=255,null=True)
  occ_Echeque_p =models.CharField(max_length=255,null=True)

  od_set_odl = models.CharField(max_length=255,null=True)
  od_ac_holder_nm =models.CharField(max_length=255,null=True)
  od_acc_no =models.IntegerField(null=True) 
  od_ifsc_code =models.IntegerField(null=True)
  od_swift_code =models.IntegerField(null=True)
  od_bank_name =models.CharField(max_length=255,null=True) 
  od_branch =models.CharField(max_length=255,null=True)
  od_SA_cheque_bk =models.CharField(max_length=255,null=True)
  od_Echeque_p =models.CharField(max_length=255,null=True)

  

  statutory_details=models.CharField(max_length=255,null=True)

  type_of_ledger = models.CharField(max_length=100,null=True)
  rounding_method = models.CharField(max_length=100,null=True)
  rounding_limit = models.IntegerField(blank=True, null=True, default=None)
  GST_Applicable = models.CharField(max_length=100,null=True)
  Alter_GST_Details= models.CharField(max_length=100,null=True)
  Appropriate=models.CharField(max_length=100,null=True)
  Types_of_supply=models.CharField(max_length=100,null=True)

  type_duty_tax = models.CharField(max_length=100,null=True)
  tax_type = models.CharField(max_length=100,null=True)
  percentage_of_calcution = models.CharField(max_length=100,null=True)
  rond_method = models.CharField(max_length=100,null=True)
  rond_limit = models.IntegerField(blank=True, null=True, default=None)

  balance_billbybill = models.CharField(max_length=100,null=True)
  credit_period = models.CharField(max_length=100,null=True)
  creditdays_voucher = models.CharField(max_length=100,null=True)

  def _str_(self):
        return self.name 






        

