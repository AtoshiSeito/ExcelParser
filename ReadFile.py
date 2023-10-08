import pandas as pd
import openpyxl
from openpyxl.utils import get_column_letter

def readFiles(filepath):
    filepath, dir = filepath
    DATA = []
    # add names to new column:
    Headers = ['FacilityCode', 'PolicyNumber', 'PolicyID', 'CropYear', 'YearPolicyTransactionID',
               'PolicyTransactionID', 'PolicyTransactionTypeTitle',
               'PolicyTransactionStatusTitle', 'BrokerName', 'InsuredName', 'CoverTypeName',
               'SeasonName', 'EventName', 'InceptionDate',
               'FinalRevisionDate', 'EffectiveDate', 'ExpiryDate', 'BindDate', 'QuoteDate',
               'QuoteExpiryDate', 'LatestPolicyTransaction', 'IsReversal', 'HasBeenReversed', 'ReversedByPolicyTransactionID',
               'ReplacingPolicyTransactionID', 'PercentageToCharge', 'AfterOrOnFRD', 'Premium', 'ReduceCommission', 
               'OrigBrokerCommRate', 'NewBrokerCommRate']
    df = pd.read_pickle(f'{dir}/{filepath}')
    try:
        df = df[Headers]
    except:
        print(f'{filepath} error!')
        return 0, filepath, pd.DataFrame()
    Number = len(df)
    df = df.fillna(0)
    tmp = df[Headers[:6]+['Premium', 'PercentageToCharge']]
    tmp = tmp.groupby(Headers[:6]).sum().reset_index()
    df = df.groupby(Headers[:6]).agg('first').reset_index()
    for i, row in tmp.iterrows():
        df.loc[i, 'Premium'] = row['Premium']
        df.loc[i, 'PercentageToCharge'] = row['PercentageToCharge']
    print(f'{filepath} OK')
    return Number, filepath, df
