from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import TextField
import uuid

# Create your models here.
class CataxDBnew(models.Model):
    txnID = models.CharField(max_length=300,primary_key=True,default=uuid.uuid4,editable=False)
    
    accountID = models.CharField(max_length=20)
    #accountType= models.IntegerField(default=0)
    accountType = models.CharField(max_length=10)
    userID = models.CharField(max_length=20,blank=True)
    
    txnEntryRoute =models.CharField(max_length=10,blank=True)
    txn=models.CharField(max_length=20,blank=True)
    txnType=models.CharField(max_length=10,blank=True, null=True)
    txnSubType=models.CharField(max_length=10,blank=True, null=True) 
    txnClaimedDateTime=models.DateTimeField(null=True, blank=True)
    txnExchangeDate=models.CharField(max_length=100,null=True, blank=True)
    exchangeTxnID=models.CharField(max_length=500,blank=True, null=True)
    
    fees =models.FloatField(default= 0,null=True, blank=True)
    feeCurrency=models.CharField(max_length=100,blank=True, null=True)
    txnHash=models.CharField(max_length=500,blank=True, null=True) 
    txnCustomerMemo=models.TextField(null=True, blank=True)
    txnExchangeMemo=models.TextField(null=True, blank=True)
    txnAuditorMemo=models.TextField(null=True, blank=True)
    
    txnStatus =models.CharField(max_length=50,blank=True,null=True)
    createdOn=models.DateTimeField(auto_now_add=True)
    updatedOn=models.DateTimeField(null=True, blank=True)
    txnVersion=models.SmallIntegerField(null=True, blank=True)
    creditedCoins=models.FloatField(null=True, blank=True)
    creditCurrency=models.CharField(max_length=50,blank=True, null=True)
    
    creditBaseAmount =models.FloatField(null=True, blank=True)
    creditBaseCurrency=models.CharField(max_length=50,blank=True, null=True)
    debitedFromAccountID=models.CharField(max_length=100,blank=True, null=True) 
    toCryptoWallet=models.CharField(max_length=1000,blank=True, null=True)
    debitCoins=models.FloatField(null=True, blank=True)
    debitCurrency=models.CharField(max_length=50,blank=True, null=True)
    
    debitBaseAmount =models.FloatField(null=True, blank=True)
    debitBaseCurrency=models.CharField(max_length=50,blank=True, null=True)
    creditedToAccountID=models.CharField(max_length=100,blank=True, null=True) 
    fromCryptoWallet=models.CharField(max_length=1000,blank=True, null=True)
    isReconciled=models.BooleanField(default=0)
    isDeleted=models.BooleanField(default=0)
    
    isAnalyzed =models.BooleanField(default=0)
    totalValueofTransaction=models.FloatField(null=True, blank=True)
    totalValueCurrency=models.CharField(max_length=50,blank=True, null=True) 
    
    


    
    

    #age =models.IntegerField(default=0, validators=[MinValueValidator(18),MaxValueValidator(100)])
    #age =models.IntegerField(default=0)
