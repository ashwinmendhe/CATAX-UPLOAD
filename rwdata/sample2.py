import pandas as pd

file = ('bitbnsBuySale.csv')
df = pd.read_csv('bitbnsBuySale.csv', usecols= ['Time', 'Crypto_Amt' ])
#print(df)

df2 = pd.read_csv('bitbnsBuySale.csv')
#print(df2(2,2))

#print(df2.head(2))
print(len(df2))
print(df2['Coin'][3])
#print(df2[1])

def dataRead_coindcx(new_data,user_id,account_id):
    global newrow
    wbRead= openpyxl.load_workbook(new_data)
    wbRead= pd.read_csv(new_data)
    #print(wbRead)
    row=len(wbRead)
    print("in read coindcx row is: ", row)
    newrow = newrow +row
    coindcxmain(wbRead,row,user_id,account_id)
    return newrow
def coindcxmain(wbRead,row,user_id,account_id):
    global i
    for i in range(0, row):
        txnExchangeDateTime = wbRead['Created At'][i]
        #print("in dcx main : ", txnExchangeDateTime)
        accountID=account_id
        accountType = 'Exchange'
        userID=user_id
        txnEntryRoute='Import'
        txnVersion = '1'
        txnStatus = 'Processing'
            
        WhosWallet='Customer Crypto wallet'
        WhoAccountID = 'Customer Crypto ID'
        valuenew = wbRead['Side'][i]
        txnExchangeMemo = wbRead['Status'][i]
        feeCurrency = 'Crypto'
        CurrencyName =wbRead['Currency'][i]
        totalValueCurrency='INR'
        exchangeTxnID = 'Null'
        totalValueofTransaction = wbRead['Total Amount'][i]
#-----------------for buy and sell--------------------------------------------------------

        if valuenew == 'BUY':
            txnType = 'Credit'
            txnSubType='Buy'
            creditedCoins =  wbRead['Total Quantity'][i]
            debitBaseAmount = wbRead['Price Per Unit'][i]
                
            val=CataxDBnew(accountID=accountID,accountType = accountType,userID=userID,
            txn=valuenew,txnEntryRoute=txnEntryRoute,txnType = txnType,
            txnSubType= txnSubType,creditedCoins=creditedCoins,txnExchangeDate =txnExchangeDateTime,
            debitBaseAmount=debitBaseAmount,txnExchangeMemo =txnExchangeMemo,creditCurrency=CurrencyName,
            feeCurrency = feeCurrency,totalValueofTransaction = totalValueofTransaction,
            txnStatus = txnStatus,txnVersion =txnVersion,toCryptoWallet=WhosWallet,
            creditedToAccountID=WhoAccountID,exchangeTxnID = exchangeTxnID,txnHash=exchangeTxnID,
            totalValueCurrency = totalValueCurrency)
            val.save()  
        elif valuenew == 'SELL':
            txnType = 'Debit'
            txnSubType='Sell'
            debitCoins = wbRead['Total Quantity'][i]
            creditBaseAmount = wbRead['Price Per Unit'][i]

            val=CataxDBnew(accountID=accountID,accountType = accountType,userID=userID,
            txn=valuenew, txnEntryRoute=txnEntryRoute,txnType = txnType,
            txnSubType= txnSubType,txnExchangeDate =txnExchangeDateTime,txnExchangeMemo =txnExchangeMemo,
            debitCoins=debitCoins,creditBaseAmount=creditBaseAmount,debitCurrency=CurrencyName,
            debitedFromAccountID=WhoAccountID,feeCurrency = feeCurrency,
            totalValueofTransaction = totalValueofTransaction,txnStatus = txnStatus,txnVersion =txnVersion,
            fromCryptoWallet=WhosWallet,exchangeTxnID = exchangeTxnID,txnHash=exchangeTxnID,
            totalValueCurrency = totalValueCurrency)
            val.save() 