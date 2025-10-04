import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged_table = sales.merge(product, on = 'product_id', how = 'left')
    return merged_table[['product_name', 'year', 'price']]

    