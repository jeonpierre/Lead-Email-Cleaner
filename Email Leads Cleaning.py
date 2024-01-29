import pandas as pd
import re


def Clean_Data():
    df = pd.read_csv(['Name-of-File'])

    df.dropna(subset=['email'], inplace=True)
    
    df.drop_duplicates(subset=['email'], keep='first', inplace=True)
    
    df.dropna(subset=['email'], inplace=True)
    
    df.to_csv('cleaned_thirty_k_leads.csv', index=False)

    df['email'] = df['email'].str.lower()

    pattern = r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?)$'

    df = df[df['email'].str.match(pattern)]
    
    common_typo_list = ['gmial.com', 'hotmial.com', 'yahho.com']
    
    df = df[~df['email'].isin(common_typo_list)]






