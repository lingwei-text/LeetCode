import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    filtered_customer = customer[(customer['referee_id'].isna()) | (customer['referee_id']!=2)][['name']]
    return filtered_customer
    