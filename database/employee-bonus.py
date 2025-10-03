import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged_table = employee.merge(bonus, how = 'left', on = 'empId')
    filtered_table = merged_table[(merged_table['bonus']<1000) | (merged_table['bonus'].isna())][['name','bonus']]
    return filtered_table.sort_values('name')
    