import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')
    weather['previousTemperature'] = weather['temperature'].shift(1)
    weather['previousDate']= weather['recordDate'].shift(1)
    return weather[(weather['temperature']> weather['previousTemperature'])& (weather['recordDate']-weather['previousDate']== pd.Timedelta(days=1))][['id']]