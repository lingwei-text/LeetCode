import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    filtered_cinema = cinema[ (cinema['id']%2 == 1) & (cinema['description']!= 'boring')]
    return filtered_cinema.sort_values('rating', ascending = False)