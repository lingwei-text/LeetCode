import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers[['count']] = my_numbers.groupby('num', as_index = False)[['num']].count()
    filtered_
    