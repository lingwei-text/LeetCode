import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge1 = sales_person.merge(orders, how = 'left', on = 'sales_id')
    merge2 = merge1.merge(company, how = 'left', on = 'com_id')
    red_sales = merge2[merge2['name_y']=='RED'][['name_x']]
    filtered_sales = merge2[~merge2['name_x'].isin(red_sales)][['name_x']]
    return filtered_sales

    