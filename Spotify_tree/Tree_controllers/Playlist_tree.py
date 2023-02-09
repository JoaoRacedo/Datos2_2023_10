from .Playlist_node import Playlist_node
from .User_node import User_node
from .Genre_node import Genre_node
from .Song_node import Song_node

class Playlist_tree:
    def __init__(self, playlist_name: str):
        self.playlist_root = Playlist_node(playlist_name) # Root node
    
    def __str__(self):
        return "La raiz es la "+ str(self.playlist_root)
    
    def insert_user(self, values: list): # NEEDS improvement!
        if values is None:
            return
        else:
            for value in values:
                user_node = User_node(value) # user name is value
                self.playlist_root.user_nodes.append(user_node)
            return self.playlist_root
        
    def insert_genre_to_user(self, values: list):
        user_node = self.User_search(values[0])
        if (user_node is not None):
            if (values[1] is not None):
                for genre in values[1]:
                    genre_node = self.insert_genre(user_node, genre)
        else:
            print("User does not exist")
        return self.playlist_root

    def insert_genre(self, user_node: User_node, genre: str):
        """
        Creates the child genre nodes and the corresponding relation with their user
        parent node
        Attributes
        ----------
        user_node: Node. Node object with the information of the parent of the children
        genre: str. value to create the node.
        """ 
        genre_node = Genre_node(genre)
        user_node.genre_nodes.append(genre_node)
    
    def User_search(self, value: str):
        """
        Searches and returns the object Node if it is present in the tree.
        Attributes
        ----------
        value: str. user info to be searched in the tree.
        """
        if self.playlist_root is None:
            return None
        traversed = []
        traversed.extend(self.playlist_root.user_nodes)

        while traversed != []:
            if traversed[0].user_name == value:
                return traversed[0]
            traversed.pop(0)
        return None
    
    
    def insert_song_genre_user(self, values: list):
        user_node = self.User_search(values[0]) # user name
        if (user_node is not None):
            genres_node_list = self.Multiple_genres_add(user_node , values[3]) # list of genres of specific track
            if (genres_node_list is not None):
                if (values[1] is not None):
                    for music_genre in genres_node_list:
                        song_node = Song_node(values[2], values[1])
                        music_genre.song_nodes.append(song_node)
            else:
                print("Genre does not exist")
        else:
            print("User does not exist")
        return self.playlist_root
    
    def Multiple_genres_add(self, user: User_node, value: list):
        """
        Searches and returns multiple object Node.
        Attributes
        ----------
        user: User_node. Object where we are going to search if genre node with
            value exist 
        value: list. list of genres to search.
        """
        genres_list = []
        for music_genre in value:
            possible_genre = self.genre_serch(user, music_genre)
            if (possible_genre is not None):
                genres_list.append(possible_genre)
        return genres_list

    def genre_serch(self, user: User_node, value: str):
        """
        Searches and returns the object Node if it is present in the tree.
        Attributes
        ----------
        user: User_node. Object where we are going to search if genre node with
            value exist 
        value: str. music genre.
        """
        traversed = []
        traversed.extend(user.genre_nodes)
        while traversed != []:
            if traversed[0].genre_name == value: # check if genre_name is the genre we are looking for
                return traversed[0]
            traversed.pop(0)
        return None