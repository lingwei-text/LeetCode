import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    users['boo'] = users['mail'].str.match(pattern, na = False)
    return users[users['boo'] == True][['user_id', 'name', 'mail']]
    