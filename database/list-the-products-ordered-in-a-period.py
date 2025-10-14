import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders['year_month'] = orders['order_date'].dt.strftime('%Y-%m')
    orders_sum = orders.groupby(['product_id', 'year_month'], as_index = False)[['unit']].sum()
    id = orders_sum[(orders_sum['unit']>=100) & (orders_sum['year_month'].str[-2:].astype(int) == 2)]
    id = id[['product_id', 'unit']]
    merge = id.merge(products, on = 'product_id', how = 'left')
    return merge[['product_name', 'unit']]

    