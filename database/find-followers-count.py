import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    count = followers.groupby('user_id', as_index = False).agg(
        followers_count = ('follower_id', 'nunique')
    )
    return count.sort_values('user_id')

    