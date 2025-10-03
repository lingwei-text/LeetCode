import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(orders, how = 'left', left_on = 'id', right_on = 'customerId')
    filtered = merged[merged['id_y'].isna()][['name']]
    return filtered.rename(columns = {'name': 'Customers'})
    