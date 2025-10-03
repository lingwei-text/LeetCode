import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders_agg = orders.groupby('customer_number', as_index = False)[['order_number']].count()
    filtered_orders = orders_agg.sort_values('order_number', ascending = False).head(1)
    return filtered_orders[['customer_number']]
    