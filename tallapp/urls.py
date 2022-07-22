from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    
    path('searchbank',views.searchbank,name='searchbank'),
    path('searchledger',views.searchledger,name='searchledger'),
    path('searchbank1',views.searchbank1,name='searchbank1'),
    path('load_create_ledgers',views.load_create_ledgers,name='load_create_ledgers'),
    path('deposit/<int:id>',views.deposit,name='deposit'),
    path('payment_advice/<int:id>',views.payment_advice,name='payment_advice'),
    path('reconciliation/<int:id>',views.reconciliation,name='reconciliation'),
]  