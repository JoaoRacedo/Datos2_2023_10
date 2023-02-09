class Genre_node:
    def __init__(self, genre_name: str, song_nodes: list = None):
        self.genre_name = genre_name
        if song_nodes is not None:
            self.song_nodes = song_nodes
        else:
            self.song_nodes = []
    
    def __str__(self):
        return "Genre name is "+ str(self.genre_name)
    
    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return len(self.song_nodes)