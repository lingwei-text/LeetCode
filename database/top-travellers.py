import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    dis = rides.groupby('user_id', as_index = False)['distance'].sum()
    merge = users.merge(dis, left_on = 'id', right_on = 'user_id', how = 'left')
    result = merge[['name', 'distance']].sort_values(['distance', 'name'], ascending = [False, True]).rename(columns = {'distance':'travelled_distance'})
    return result.fillna(0)
    
    