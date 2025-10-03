import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged_table = employee.merge(employee, left_on = 'managerId', right_on = 'id', suffixes=['_emp','_man'], how = 'inner')
    filtered_table = merged_table[merged_table['salary_emp']>merged_table['salary_man']][['name_emp']]
    return filtered_table.rename(columns = {'name_emp':'Employee'})
    
    