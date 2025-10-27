import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    count = employees.groupby('reports_to',as_index = False).agg(
        reports_count = ('reports_to', 'size'),
        average_age = ('age', 'mean')
    )
    merge = count.merge(employees, how = 'inner', left_on = 'reports_to', right_on = 'employee_id')
    merge['average_age'] = (merge['average_age'] + 1e-12).round()
    return merge[['employee_id', 'name', 'reports_count', 'average_age']].sort_values('employee_id')


