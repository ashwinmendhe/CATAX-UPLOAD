from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CataxDBnew
# Register your models here.

@admin.register(CataxDBnew)
class CataxDBnewAdmin(ImportExportModelAdmin):
    list_display = ('txnID','accountID','accountType','userID','txnEntryRoute','txn','txnType', 'txnSubType','txnClaimedDateTime','txnExchangeDate','exchangeTxnID',
 'fees','feeCurrency','txnHash','txnCustomerMemo','txnExchangeMemo','txnAuditorMemo','txnStatus','createdOn','updatedOn','txnVersion',
'creditedCoins','creditCurrency','creditBaseAmount','creditBaseCurrency','debitedFromAccountID','toCryptoWallet',
'debitCoins','debitCurrency','debitBaseAmount','debitBaseCurrency','creditedToAccountID','fromCryptoWallet','isReconciled',
'isDeleted','isAnalyzed','totalValueofTransaction' , 'totalValueCurrency')
