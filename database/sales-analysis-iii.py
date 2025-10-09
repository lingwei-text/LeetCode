import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(product, sales, on='product_id')

    START_DATE = '2019-01-01'
    END_DATE = '2019-03-31'

    all_products = df['product_id'].unique()

    out_of_window_sales = df[
        (df['sale_date'] < START_DATE) | (df['sale_date'] > END_DATE)
    ]
    products_sold_outside = out_of_window_sales['product_id'].unique()

 
    products_only_in_window = set(all_products) - set(products_sold_outside)

    result_df = product[product['product_id'].isin(products_only_in_window)]

    return result_df[['product_id', 'product_name']]