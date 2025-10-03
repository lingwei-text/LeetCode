import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    e = person[person.duplicated(subset = ['email'], keep =False)]
    f = e.drop_duplicates(subset = ['email'], keep ='first')
    return f[['email']].rename(columns = {'email': 'Email'})
