import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(prices, units_sold, how='left', on='product_id')
    merged_df = merged_df[(merged_df['purchase_date'].isna()) | ((merged_df['purchase_date'] >= merged_df['start_date']) & (merged_df['purchase_date'] <= merged_df['end_date']))]
    # Fill NaN values in units column with 0
    merged_df['units'].fillna(0, inplace=True)
    print(merged_df)

    result_df = merged_df.groupby(by='product_id').apply(lambda x: round((x['price']*x['units']).sum() / x['units'].sum(), 2) if x['units'].sum() != 0 else 0).reset_index(name='average_price')

    return result_df
    