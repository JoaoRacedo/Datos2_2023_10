from spotify_controller import Spotify_Stuff
from Preprocesing_controller import save_data_list_to_csv, read_data_from_csv, preprocess_df, get_list_user_unique_genres, get_list_from_df
from Tree_controllers.Playlist_tree import Playlist_tree

### Spotify stuff
#spotify = Spotify_Stuff()
#url_playlist = "https://open.spotify.com/playlist/7y1yhwfkpWxUNH7K2TUY4X?si=kasgGVgtR-KEOaSZnzzH_g"
#id_playlist = spotify.get_id(url_playlist)
#data_list = spotify.get_playlist_items_by_id()
#save_data_list_to_csv(data_list) # culpa de JJJZ


### preprocessing stuff

data = read_data_from_csv()
processed_data = preprocess_df(data)
lista_datos_procesados = get_list_user_unique_genres(processed_data)
lista_datos = get_list_from_df(data)

### EDII stuff - Trees n

tree = Playlist_tree("EDII_playlist")

print("--------------------------")
print(tree)
print("--------------------------")

unique_users = list(processed_data["User_name"].unique())
tree.insert_user(unique_users);

print("--------------------------")
print(len(tree.playlist_root))
print(repr(tree.playlist_root.user_nodes))
print("--------------------------")

for user_genre in lista_datos_procesados:
    tree.insert_genre_to_user(user_genre)

print("--------------------------")
index = 3
print(tree.playlist_root.get_user(index))
print("The user has",len(tree.playlist_root.user_nodes[index]),"genres added to the playlist")
print(repr(tree.playlist_root.user_nodes[index].genre_nodes))
print("--------------------------")

for track_info in lista_datos:
    tree.insert_song_genre_user(track_info)

print("--------------------------")
for i in range(len(tree.playlist_root.user_nodes[index])):
    print(tree.playlist_root.user_nodes[index].genre_nodes[i])
    print(tree.playlist_root.user_nodes[index].genre_nodes[i].song_nodes)
print("--------------------------")




