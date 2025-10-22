import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    balance = transactions.groupby('account',as_index = False).agg(
        balance = ('amount','sum')
    )
    above = balance[balance['balance']>10000][['account','balance']]
    merge = above.merge(users, how = 'inner', on = 'account')
    return merge[['name', 'balance']]
    