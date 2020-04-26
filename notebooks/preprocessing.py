import pandas as pd

def create_subset(df, new_df, col_1, col_2):
    new_df = df.iloc[:, [col_1, col_2]]
    new_df.columns = ['text', 'token']
    new_df = new_df.dropna()
    return new_df