# Generated by Django 3.2.9 on 2021-11-19 06:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CataxDB',
            fields=[
                ('txnID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('accountID', models.CharField(max_length=20)),
                ('accountType', models.CharField(max_length=10)),
                ('userID', models.CharField(blank=True, max_length=20)),
                ('txnEntryRoute', models.CharField(blank=True, max_length=10)),
                ('txnType', models.CharField(blank=True, max_length=10, null=True)),
                ('txnSubType', models.CharField(blank=True, max_length=10, null=True)),
                ('txnClaimedDateTime', models.CharField(blank=True, max_length=50, null=True)),
                ('txnExchangeDate', models.CharField(blank=True, max_length=50, null=True)),
                ('exchangeTxnID', models.CharField(blank=True, max_length=5000, null=True)),
                ('fees', models.CharField(max_length=50, null=True)),
                ('feeCurrency', models.CharField(blank=True, max_length=50, null=True)),
                ('txnHash', models.CharField(blank=True, max_length=5000, null=True)),
                ('txnCustomerMemo', models.CharField(blank=True, max_length=5000, null=True)),
                ('txnExchangeMemo', models.CharField(blank=True, max_length=5000, null=True)),
                ('txnAuditorMemo', models.CharField(blank=True, max_length=5000, null=True)),
                ('txnStatus', models.CharField(blank=True, max_length=50, null=True)),
                ('createdOn', models.CharField(blank=True, max_length=50, null=True)),
                ('updatedOn', models.CharField(blank=True, max_length=50, null=True)),
                ('txnVersion', models.DecimalField(decimal_places=1, max_digits=2)),
                ('creditedCoins', models.CharField(blank=True, max_length=50, null=True)),
                ('creditCurrency', models.CharField(blank=True, max_length=50, null=True)),
                ('creditBaseAmount', models.CharField(blank=True, max_length=50, null=True)),
                ('creditBaseCurrency', models.CharField(blank=True, max_length=50, null=True)),
                ('debitedFromAccountID', models.CharField(blank=True, max_length=50, null=True)),
                ('toCryptoWallet', models.CharField(blank=True, max_length=50, null=True)),
                ('debitCoins', models.CharField(blank=True, max_length=50, null=True)),
                ('debitCurrency', models.CharField(blank=True, max_length=50, null=True)),
                ('debitBaseAmount', models.CharField(blank=True, max_length=50, null=True)),
                ('debitBaseCurrency', models.CharField(blank=True, max_length=50, null=True)),
                ('creditedToAccountID', models.CharField(blank=True, max_length=50, null=True)),
                ('fromCryptoWallet', models.CharField(blank=True, max_length=50, null=True)),
                ('isReconciled', models.CharField(blank=True, default=0, max_length=50, null=True)),
                ('isDeleted', models.CharField(blank=True, default=0, max_length=50, null=True)),
                ('isAnalyzed', models.CharField(blank=True, default=0, max_length=50, null=True)),
                ('totalValueofTransaction', models.CharField(blank=True, max_length=50, null=True)),
                ('totalValueCurrency', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
