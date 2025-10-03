import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(['player_id', 'event_date'], ascending = [True, True])
    activity = activity.groupby('player_id', as_index = False)[['event_date']].min()
    activity_rename = activity[['player_id', 'event_date']].rename(columns = {'event_date':'first_login'})
    return activity_rename.sort_values('player_id')