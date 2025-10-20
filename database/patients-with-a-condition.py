import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = r'\bDIAB1\b'
    patients['boo'] = patients['conditions'].str.contains(pattern, na = False)
    return patients[patients['boo']==True][['patient_id', 'patient_name', 'conditions']]

    