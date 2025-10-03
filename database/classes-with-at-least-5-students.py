import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    count = courses.groupby('class', as_index = False)[['student']].count()
    filter = count[count['student']>=5][['class']]
    return filter
    