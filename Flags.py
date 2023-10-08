import pandas as pd
import openpyxl
from openpyxl.utils import get_column_letter

def Flags(Dict):

    NumberCounter = 0
    PolicePaidCounter = 0
    PoliceInvoicedCounter = 0
    (filepath, DF) = Dict
    for i, row in DF.iterrows():
        NumberCounter += 1
        if DF.iloc[i]['Starting state'] == 1:
            NumberCounter = 1
            PolicePaidCounter = 0
            PoliceInvoicedCounter = 0

        if float(row['Term Premium Fin']) == float(row['Premium']):
            DF.loc[[i], 'Paid'] = 1
            PolicePaidCounter = 1
        if row['PercentageToCharge']:
            DF.loc[[i], 'Invoiced'] = 1
            PoliceInvoicedCounter = 1
    
        if (DF.iloc[i]['Ending state'] == 1):
            indexes = DF[(DF['YearPolicyTransactionID'] == row.loc['YearPolicyTransactionID']) & (DF['CropYear'] == row.loc['CropYear']) & (DF['PolicyNumber'] == row.loc['PolicyNumber'])].index
            for index in indexes:
                if PolicePaidCounter:
                    DF.loc[[index], 'Paid Police'] = 1
                if PoliceInvoicedCounter:
                    DF.loc[[index], 'Invoiced Police'] = 1
                DF.loc[[index], 'Sum of transaction'] = NumberCounter

        DF.loc[[i], 'Number of transaction'] = NumberCounter
    print('Ok')
    return filepath, DF
