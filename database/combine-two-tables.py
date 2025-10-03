import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Merge on personId using left join
    merged_table = person.merge(address, on="personId", how="left")
    final_result = merged_table[['firstName', 'lastName', 'city', 'state']]
    return final_result
