import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    department = department.groupby(['id', 'month'], as_index=False)['revenue'].sum()
    months = ['Jan', 'Feb', "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    dep_pivot = department.pivot(index = 'id', columns ='month', values = 'revenue').reindex(columns = months)
    
    dep_pivot.columns = [f"{col}_Revenue" for col in dep_pivot.columns]
    dep_pivot = dep_pivot.reset_index()
    return dep_pivot
