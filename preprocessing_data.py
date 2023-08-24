import pandas as pd
import re

def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('\n', '', text)
    text = re.sub(r'[^\w]', ' ', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def cleanning_data(df):
    df['Plot'] = df['Plot'].apply(clean_text)
    df['Genre'] = df['Genre'].apply(clean_text)
    return df

class DataLoader:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def get_optimal_data_frame(self, release_year, genre=None):
        df = self.df[self.df['Release Year'] == release_year]
        if genre is not None:
            df = df[df['Genre'] == genre]
        return df
    
    def cleanning_data(self,release_year,genre=None):
        self.df = self.get_optimal_data_frame(release_year, genre)
        self.df['Plot'] = self.df['Plot'].apply(clean_text)
        self.df['Genre'] = self.df['Genre'].apply(clean_text)
        return self.df

