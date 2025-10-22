import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(['machine_id', 'process_id', 'activity_type'], ascending = [True, True, False])
    activity['time'] = activity['timestamp'] - activity['timestamp'].shift(1)
    activity = activity[activity['activity_type']=='end']
    average = activity.groupby('machine_id', as_index = False)['time'].mean()
    return average[['machine_id', 'time']].rename(columns = {'time':'processing_time'}).round(3)
