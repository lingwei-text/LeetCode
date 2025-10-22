import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_user = users['user_id'].nunique()
    register_user = register.groupby('contest_id', as_index = False)['user_id'].nunique()
    register_user['percentage'] = (register_user['user_id']/total_user)*100
    return register_user.sort_values(['percentage','contest_id'], ascending = [False, True])[['contest_id', 'percentage']].round(2)
    

    