import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    filtered_table = actor_director.groupby(['actor_id', 'director_id'], as_index = False)[['timestamp']].count()
    return filtered_table[filtered_table['timestamp']>=3][['actor_id', 'director_id']]
    