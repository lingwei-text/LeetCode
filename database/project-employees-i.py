import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged_table = project.merge(employee, how = 'left', on = 'employee_id')
    avg = merged_table.groupby('project_id', as_index = False)[['experience_years']].mean()
    avg[['average_years']] = avg[['experience_years']].round(2)
    return avg[['project_id', 'average_years']]

    