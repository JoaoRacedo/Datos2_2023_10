class Playlist_node:
    def __init__(self, playlist_name: str, user_nodes: list = None):
        self.playlist_name = playlist_name
        if user_nodes is not None:
            self.user_nodes = user_nodes
        else:
            self.user_nodes = []
    
    def __str__(self):
        return "Playlist name is "+ str(self.playlist_name)
    

    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return len(self.user_nodes)

    def get_user(self, index: int = 0):
        return self.user_nodes[index]