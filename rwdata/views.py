from django.shortcuts import render,redirect
from .models import CataxDBnew
from .resources import CataxDBnewResource
from django.contrib import messages
from tablib import Dataset
import openpyxl
from openpyxl import Workbook
import datetime
# Create your views here.
i = 1
j = 1
newrow=0



#-------------binance----------------------------------
def binancemain(shRead1,row,column,sheets,user_id,account_id):
    global i, j
    for i in range(1, row+1):
        for j in range(1,column+1):
            txnExchangeDateTime =shRead1.cell(i,7).value
            python_datetime='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    
            accountID=account_id
            accountType = 'Exchange'
            userID=shRead1.cell(i,1).value
            txnEntryRoute='Import'
            feeCurrency = 'Crypto'
            txnVersion = '1.0'
            txnStatus = 'Processing'
            ExchangeName='Binanace Exchange'
            WhosWallet='Customer Crypto wallet'
            valuenew = sheets
            txnExchangeMemo = 'Success'
            totalValueofTransaction = 'Null'
            totalValueCurrency = 'Null'
            CurrencyName = shRead1.cell(i,2).value
            exchangeTxnID = shRead1.cell(i,6).value
  #---------for credit-------------------------------------------------
            if valuenew == 'Deposit History':
                txnType = 'Credit'
                txnSubType='Deposit'
                creditedCoins =  shRead1.cell(i,3).value
                debitBaseAmount = 'Null'
                
                val=CataxDBnew(accountID=accountID,accountType = accountType,
                    userID=userID, txn=txnSubType,txnEntryRoute=txnEntryRoute,txnType = txnType,txnSubType= txnSubType,
                    creditedCoins=creditedCoins,txnExchangeDate =txnExchangeDateTime,
                    debitBaseAmount=debitBaseAmount,txnExchangeMemo =txnExchangeMemo,
                    creditCurrency=CurrencyName,debitedFromAccountID=ExchangeName,feeCurrency = feeCurrency,
                    totalValueofTransaction = totalValueofTransaction,txnStatus = txnStatus,txnVersion =txnVersion,
                    toCryptoWallet=WhosWallet, createdOn = python_datetime,exchangeTxnID = exchangeTxnID, 
                    txnHash=exchangeTxnID,totalValueCurrency = totalValueCurrency)
                val.save()  

#---------for Debit-------------------------------------------------                
            else:
                if valuenew == 'Withdrawal History':
                    txnType = 'Debit'
                    txnSubType='Withdrawal'
                    debitCoins = shRead1.cell(i,3).value
                    creditBaseAmount = 'Null'        
                    
                    val=CataxDBnew(accountID=accountID,accountType = accountType,
                    userID=userID,txn=valuenew, txnEntryRoute=txnEntryRoute,txnType = txnType,txnSubType= txnSubType,
                        txnExchangeDate =txnExchangeDateTime,txnExchangeMemo =txnExchangeMemo,
                        debitCoins=debitCoins,creditBaseAmount=creditBaseAmount,
                        debitCurrency=CurrencyName,creditedToAccountID=ExchangeName,feeCurrency = feeCurrency,
                        totalValueofTransaction = totalValueofTransaction,txnStatus = txnStatus,txnVersion =txnVersion,
                        fromCryptoWallet=WhosWallet, createdOn = python_datetime,exchangeTxnID = exchangeTxnID, 
                        txnHash=exchangeTxnID,totalValueCurrency = totalValueCurrency)
                    val.save()

#-------------End---------------------------------------
          

#-------------end----------------------------------
#-------------Koinex function---------------------------
def Koinexmain(shRead1,row,column,sheets,user_id,account_id):
    global i, j
    for i in range(1, row+1):
        for j in range(1,column+1):
            txnExchangeDateTime =shRead1.cell(i,1).value
            python_datetime='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    
            accountID=account_id
            accountType = 'Exchange'
            userID=user_id
            txnEntryRoute='Import'
            feeCurrency = 'Crypto'
            txnVersion = '1.0'
            txnStatus = 'Processing'
            ExchangeName='Koinex Exchange'
            WhosWallet='Customer Crypto wallet'
            valuenew = shRead1.cell(i,j).value
            txnExchangeMemo = 'Success'
            totalValueofTransaction = shRead1.cell(i,6).value
            totalValueCurrency = 'INR'
            CurrencyName = whichcoin(shRead1.cell(i,2).value)
            exchangeTxnID = 'Null'
            
#---------for credit-------------------------------------------------
            if valuenew == 'BUY' or valuenew == 'Recieve' or valuenew == 'Welcome':
                txnType = 'Credit'
                txnSubType=credit(valuenew)
                creditedCoins =  shRead1.cell(i,4).value
                debitBaseAmount = shRead1.cell(i,5).value
                
                val=CataxDBnew(accountID=accountID,accountType = accountType,
                    userID=userID, txn=valuenew,txnEntryRoute=txnEntryRoute,txnType = txnType,txnSubType= txnSubType,
                    creditedCoins=creditedCoins,txnExchangeDate =txnExchangeDateTime,
                    debitBaseAmount=debitBaseAmount,txnExchangeMemo =txnExchangeMemo,
                    creditCurrency=CurrencyName,debitedFromAccountID=ExchangeName,feeCurrency = feeCurrency,
                    totalValueofTransaction = totalValueofTransaction,txnStatus = txnStatus,txnVersion =txnVersion,
                    toCryptoWallet=WhosWallet, createdOn = python_datetime,exchangeTxnID = exchangeTxnID, 
                    txnHash=exchangeTxnID,totalValueCurrency = totalValueCurrency)
                val.save()  

#---------for Debit-------------------------------------------------                
            else:
                if valuenew == 'SELL' or valuenew == 'Send' or valuenew =='Sell Cancel':
                    txnType = 'Debit'
                    txnSubType=debit(valuenew) 
                    debitCoins = shRead1.cell(i,4).value
                    creditBaseAmount = shRead1.cell(i,5).value                
                    
                    val=CataxDBnew(accountID=accountID,accountType = accountType,
                    userID=userID,txn=valuenew, txnEntryRoute=txnEntryRoute,txnType = txnType,txnSubType= txnSubType,
                        txnExchangeDate =txnExchangeDateTime,txnExchangeMemo =txnExchangeMemo,
                        debitCoins=debitCoins,creditBaseAmount=creditBaseAmount,
                        debitCurrency=CurrencyName,creditedToAccountID=ExchangeName,feeCurrency = feeCurrency,
                        totalValueofTransaction = totalValueofTransaction,txnStatus = txnStatus,txnVersion =txnVersion,
                        fromCryptoWallet=WhosWallet, createdOn = python_datetime,exchangeTxnID = exchangeTxnID, 
                        txnHash=exchangeTxnID,totalValueCurrency = totalValueCurrency)
                    val.save()

#-------------End---------------------------------------



#-------------Zebpay function---------------------------
def Zebmain(shRead1,row,column,sheet,length,user_id,account_id):
    global i, j
    for i in range(1, row+1):
        for j in range(1,column+1): 
            txnExchangeDateTime =shRead1.cell(i,1).value
            python_datetime='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            
            accountID=account_id
            accountType = 'Exchange'
            userID=user_id
            txnEntryRoute='Import'
            feeCurrency = 'Crypto'
            txnVersion = '1.0'
            txnStatus = 'Processing'
            ExchangeName='Zebpay Exchange'
            WhosWallet='Customer Crypto wallet'
            valuenew = shRead1.cell(i,j).value
            txnExchangeMemo = shRead1.cell(i,5).value
            #x = shRead1.cell(i,3).value * shRead1.cell(i,4).value
            #totalValueofTransaction = shRead1.cell(i,3).value * shRead1.cell(i,4).value
            totalValueCurrency = 'INR'
            CurrencyName = sheet[length]
            exchangeTxnID = shRead1.cell(i,9).value

#---------for credit-------------------------------------------------
            if valuenew == 'Buy' or valuenew == 'Recieve' or valuenew == 'Internal Recieve' or valuenew == 'Welcome':
                txnType = 'Credit'
                txnSubType=credit(valuenew)
                creditedCoins =  shRead1.cell(i,4).value               
                debitBaseAmount = shRead1.cell(i,3).value
                totalValueofTransaction = creditedCoins * debitBaseAmount
                val=CataxDBnew(accountID=accountID,accountType = accountType,
                    userID=userID, txn=valuenew, txnEntryRoute=txnEntryRoute,txnType = txnType,txnSubType= txnSubType,
                    creditedCoins=creditedCoins,txnExchangeDate =txnExchangeDateTime,
                    txnExchangeMemo = txnExchangeMemo,debitBaseAmount =debitBaseAmount,
                    creditCurrency=CurrencyName,debitedFromAccountID=ExchangeName,feeCurrency = feeCurrency,
                    totalValueofTransaction = totalValueofTransaction,txnStatus = txnStatus,txnVersion = txnVersion,
                    toCryptoWallet=WhosWallet, createdOn = python_datetime, exchangeTxnID = exchangeTxnID, 
                    txnHash=exchangeTxnID,totalValueCurrency = totalValueCurrency)
                val.save()  

#---------for Debit-------------------------------------------------                
            else:
                if valuenew == 'Sell' or valuenew == 'Send' or valuenew == 'Internal Send' or valuenew =='Sell Cancel':
                    txnType = 'Debit'
                    txnSubType=debit(valuenew) 
                    debitCoins = shRead1.cell(i,4).value              
                    creditBaseAmount = shRead1.cell(i,3).value 
                    totalValueofTransaction = debitCoins * creditBaseAmount
                    val=CataxDBnew(accountID=accountID,accountType = accountType,
                    userID=userID,txn=valuenew, txnEntryRoute=txnEntryRoute,txnType = txnType,txnSubType= txnSubType,
                        txnExchangeDate =txnExchangeDateTime,txnExchangeMemo = txnExchangeMemo,
                        debitCoins=debitCoins,creditBaseAmount=creditBaseAmount,
                        debitCurrency=CurrencyName,creditedToAccountID=ExchangeName,feeCurrency = feeCurrency,
                        totalValueofTransaction = totalValueofTransaction
                        ,txnStatus = txnStatus,txnVersion =txnVersion,
                        fromCryptoWallet=WhosWallet, createdOn = python_datetime, 
                        exchangeTxnID = exchangeTxnID, txnHash=exchangeTxnID,totalValueCurrency = totalValueCurrency)
                    val.save()

#-------------End---------------------------------------


#-------------credit function---------------------------
def credit(typecredit):
    if typecredit == 'Buy':
           txnSubType = 'Buy'
           return txnSubType
    else:
        if typecredit == 'Recieve':
            txnSubType = 'Deposite'
            return txnSubType
            #shWrite1['G{}'.format(i)].value = 'Deposite'        
        else: 
            if typecredit == 'Welcome':
                txnSubType = 'Reward'
                return txnSubType
            else:
                if typecredit == 'Internal Recieve':
                    txnSubType = 'Deposite'
                    return txnSubType
                
           
#-------------End---------------------------------------


#-------------Debit function---------------------------
def debit(typedebit):
    if typedebit == 'Send':
        txnSubType =  'Transfer'
        return txnSubType    
    else:
        if typedebit == 'Sell':
            txnSubType =  'Sell'
            return txnSubType   
        else:
            if typedebit == 'Sell cancel':
             txnSubType =  'Sell'
             return txnSubType
            else:
               if typedebit == 'Internal Send':
                txnSubType =  'Transfer'
                return txnSubType      
        
        
    
#-------------End---------------------------------------


#-------------Found coin name---------------------------  
def whichcoin(findcoin):
    if findcoin == 'AE/INR':
        newcoin = 'AE'
        return newcoin
    else:
        if findcoin == 'AION/INR':
            newcoin = 'AION'
            return newcoin
        else:
            if findcoin == 'BAT/INR':
                newcoin = 'BAT'
                return newcoin
            else:
                if findcoin == 'BCH/INR':
                    newcoin = 'BCH'
                    return newcoin 
                else:
                    if findcoin == 'BTC/INR':
                     newcoin = 'BTC'
                     return newcoin
                    else:
                        if findcoin == 'EOS/INR':
                         newcoin = 'EOS'
                         return newcoin
                        else:
                            if findcoin == 'ETH/INR':
                             newcoin = 'ETH'
                             return newcoin
                            else:
                                if findcoin == 'GNT/INR':
                                 newcoin = 'GNT'
                                 return newcoin
                                else:
                                    if findcoin == 'LTC/INR':
                                     newcoin = 'LTC'
                                     return newcoin
                                    else:
                                        if findcoin == 'NCASH/INR':
                                         newcoin = 'NCASH'
                                         return newcoin
                                        else:
                                            if findcoin == 'NEO/INR':
                                             newcoin = 'NEO'
                                             return newcoin
                                            else:
                                                if findcoin == 'OMG/INR':
                                                 newcoin = 'OMG'
                                                 return newcoin
                                                else:
                                                    if findcoin == 'REQ/INR':
                                                     newcoin = 'REQ'
                                                     return newcoin
                                                    else:
                                                        if findcoin == 'TRX/INR':
                                                         newcoin = 'TRX'
                                                         return newcoin
                                                        else:
                                                            if findcoin == 'XLM/INR':
                                                             newcoin = 'XLM'
                                                             return newcoin
                                                            else:
                                                                if findcoin == 'XRB/INR':
                                                                 newcoin = 'XRB'
                                                                 return newcoin
                                                                else:
                                                                    if findcoin == 'XRP/INR':
                                                                     newcoin = 'XRP'
                                                                     return newcoin
                                                                    else:
                                                                        if findcoin == 'ZRX/INR':
                                                                         newcoin = 'ZRX'
                                                                         return newcoin
                           
                           

#-------------End---------------------------------------
#-------------Data Read--------------------------- 
def dataRead_zebpay(new_data,user_id,account_id):
    global newrow
    wbRead= openpyxl.load_workbook(new_data)  
    sheets=wbRead.sheetnames
    shRead1= [0]*len(sheets)
    for length in range(len(sheets)):
        shRead1[length]= wbRead[sheets[length]]
        row = shRead1[length].max_row
        column = shRead1[length].max_column
        newrow = newrow +row
        Zebmain(shRead1[length],row,column,sheets,length,user_id,account_id)
        print('Succesfully uploaded Zebpay trade data: ', length)
    return newrow
#-------------End---------------------------------------

#-------------Data Read--------------------------- 
def dataRead_koinex(new_data):
    wbRead= openpyxl.load_workbook(new_data)    
    sheets=wbRead.sheetnames
    shRead1= wbRead[sheets[0]]
    row = shRead1.max_row
    column = shRead1.max_column
    return shRead1,row,column,sheets
#-------------End---------------------------------------

#-------------Data Read--------------------------- 
def dataRead_binance(new_data,user_id,account_id):
    global newrow
    wbRead= openpyxl.load_workbook(new_data)    
    sheets=wbRead.sheetnames
    #shRead1= [0]*len(sheets)
    for length in range(len(sheets)):
        if sheets[length] == 'Deposit History' or sheets[length] == 'Withdrawal History':
            shRead1= wbRead[sheets[length]]
            row = shRead1.max_row
            column = shRead1.max_column
            newrow = newrow +row
            binancemain(shRead1,row,column,sheets[length],user_id,account_id)
    return newrow             
#-------------End---------------------------------------

#-------------Data Read--------------------------- 
def dataRead_wzirx(new_data,user_id,account_id):
    global newrow
    wbRead= openpyxl.load_workbook(new_data)    
    sheets=wbRead.sheetnames
    #shRead1= [0]*len(sheets)
    for length in range(len(sheets)):
        if sheets[length] == 'Exchange Trades' or sheets[length] == 'Withdrawal History':
            shRead1= wbRead[sheets[length]]
            row = shRead1.max_row
            column = shRead1.max_column
            newrow = newrow +row
            binancemain(shRead1,row,column,sheets[length],user_id,account_id)
    return newrow   
#-------------End---------------------------------------





#-------------Main Coding Start here---------------------------  
def simple_upload(request):
    global newrow
    if request.method == "POST":
        new_data = request.FILES['myfiles']
        user_id=request.POST.get('id')
        account_id=request.POST.get('Eid')
        exchange_name=request.POST.get('exchange')
 #--------------for zebpay-----------------------------------       
        #print(new_data,user_id,account_id,exchange_name)
        if str(exchange_name) == 'zebpay':
            count=dataRead_zebpay(new_data,user_id,account_id)
            return render(request,'result.html',{'res':count})
 #--------------zebpay end----------------------------------- 
#--------------for koinex-----------------------------------                       
        else:
            if str(exchange_name)=='koinex':
                shRead1,row,column,sheets=dataRead_koinex(new_data)
                Koinexmain(shRead1,row,column,sheets,user_id,account_id)
                return render(request,'result.html',{'res':row-1})
 #--------------koinex end----------------------------------- 
#--------------for binance-----------------------------------          
            else:
                if str(exchange_name)=='binance':
                    count=dataRead_binance(new_data,user_id,account_id)
                    print(exchange_name)
                    return render(request,'result.html',{'res':count})
#--------------binance end----------------------------------- 
#--------------for wazirx-----------------------------------                 
                else:
                    if str(exchange_name) == 'wzirx':
                        count=dataRead_wzirx(new_data,user_id,account_id)
                        return render(request,'result.html',{'res':count})
#--------------wzirx end-----------------------------------                 
    return render(request, 'upload.html')
 


#-------------End---------------------------------------