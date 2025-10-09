import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filter = views[views['author_id']==views['viewer_id']][['author_id']].rename(columns = {'author_id':'id'})
    result = filter[['id']].drop_duplicates()
    return result.sort_values('id')
    