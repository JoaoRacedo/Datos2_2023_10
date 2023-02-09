import csv
import pandas as pd
import ast
import os


def save_data_list_to_csv(lista: list):
    fields = ['User_name','Artist_name', 'Track' ,"Genres"] 
    with open('data/Playlist_data.csv', 'w') as f:
        
        csv_writer = csv.writer(f)
        csv_writer.writerow(fields)
        csv_writer.writerows(lista)

def read_data_from_csv():
    get_path = os.path.abspath(os.getcwd())
    df = pd.read_csv(get_path+"/data/Playlist_data.csv")
    return df

def unique_values_in_list_of_lists(lst: list):
    result = set(x for l in lst for x in l)
    return list(result)

def preprocess_df(df: pd.DataFrame):
    df['Genres'] = df['Genres'].map(ast.literal_eval)
    df2 = df.groupby("User_name")[["Genres"]].agg(list).reset_index()
    df2["list_unique_genres"] = df2["Genres"].map(unique_values_in_list_of_lists)
    return df2

def get_list_user_unique_genres(df: pd.DataFrame):
    list_user_genres = df[["User_name","list_unique_genres"]].values.tolist()
    return list_user_genres

def get_list_from_df(df: pd.DataFrame):
    return df.values.tolist()



