from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import TextField
import uuid

# Create your models here.
class CataxDB(models.Model):
    txnID = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    accountID = models.CharField(max_length=20)
    #accountType= models.IntegerField(default=0)
    accountType = models.CharField(max_length=10)
    userID = models.CharField(max_length=20,blank=True)
    
    txnEntryRoute =models.CharField(max_length=10,blank=True)
    txnType=models.CharField(max_length=10,blank=True, null=True)
    txnSubType=models.CharField(max_length=10,blank=True, null=True) 
    txnClaimedDateTime=models.CharField(max_length=50,blank=True, null=True)
    txnExchangeDate=models.CharField(max_length=50,blank=True, null=True)
    exchangeTxnID=models.CharField(max_length=5000,blank=True, null=True)
    
    fees =models.CharField(max_length=50,null=True)
    feeCurrency=models.CharField(max_length=50,blank=True, null=True)
    txnHash=models.CharField(max_length=5000,blank=True, null=True) 
    txnCustomerMemo=models.CharField(max_length=5000,blank=True, null=True)
    txnExchangeMemo=models.CharField(max_length=5000,blank=True, null=True)
    txnAuditorMemo=models.CharField(max_length=5000,blank=True, null=True)
    
    txnStatus =models.CharField(max_length=50,blank=True,null=True)
    createdOn=models.CharField(max_length=50,blank=True, null=True)
    updatedOn=models.CharField(max_length=50,blank=True, null=True) 
    txnVersion=models.DecimalField(max_digits=2, decimal_places=1)
    creditedCoins=models.CharField(max_length=50,blank=True, null=True)
    creditCurrency=models.CharField(max_length=50,blank=True, null=True)
    
    creditBaseAmount =models.CharField(max_length=50,blank=True,null=True)
    creditBaseCurrency=models.CharField(max_length=50,blank=True, null=True)
    debitedFromAccountID=models.CharField(max_length=50,blank=True, null=True) 
    toCryptoWallet=models.CharField(max_length=50,blank=True, null=True)
    debitCoins=models.CharField(max_length=50,blank=True, null=True)
    debitCurrency=models.CharField(max_length=50,blank=True, null=True)
    
    debitBaseAmount =models.CharField(max_length=50,blank=True,null=True)
    debitBaseCurrency=models.CharField(max_length=50,blank=True, null=True)
    creditedToAccountID=models.CharField(max_length=50,blank=True, null=True) 
    fromCryptoWallet=models.CharField(max_length=50,blank=True, null=True)
    isReconciled=models.CharField(default=0,max_length=50,blank=True, null=True)
    isDeleted=models.CharField(default=0,max_length=50,blank=True, null=True)
    
    isAnalyzed =models.CharField(default=0,max_length=50,blank=True,null=True)
    totalValueofTransaction=models.CharField(max_length=50,blank=True, null=True)
    totalValueCurrency=models.CharField(max_length=50,blank=True, null=True) 
    
    


    
    

    #age =models.IntegerField(default=0, validators=[MinValueValidator(18),MaxValueValidator(100)])
    #age =models.IntegerField(default=0)
