import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merge = visits.merge(transactions, how = 'left', on = 'visit_id')
    merge = merge[merge['transaction_id'].isna()]
    result = merge.groupby('customer_id',as_index = False).agg(
        count_no_trans=('transaction_id','size')
    )
    return result[['customer_id', 'count_no_trans']]
