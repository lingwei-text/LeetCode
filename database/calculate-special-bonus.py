import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    def compute_bonus(row):
        # If employee_id is odd AND name starts with 'M'
        if row['employee_id'] % 2 == 1 and row['name'].startswith('M'):
            return 0
        else:
            return row['salary']
    
    employees['bonus'] = employees.apply(compute_bonus, axis=1)
    
    return employees[['employee_id', 'bonus']].sort_values('employee_id')



    