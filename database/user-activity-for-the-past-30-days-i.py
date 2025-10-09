import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    end_date = pd.to_datetime('2019-07-27')
    start_date = end_date - pd.Timedelta(days = 29)
    active_user = activity[(activity['activity_date']>=start_date)&(activity['activity_date']<=end_date)]
    user_count = active_user.groupby('activity_date', as_index = False)[['user_id']].nunique()
    return user_count[['activity_date', 'user_id']].rename(columns={'activity_date':'day', 'user_id':'active_users'})