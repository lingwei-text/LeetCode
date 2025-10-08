import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers = my_numbers.groupby('num', as_index = False).size()
    filter = my_numbers[my_numbers['size']==1]
    return filter.sort_values('num', ascending = False)[['num']].head(1)

    