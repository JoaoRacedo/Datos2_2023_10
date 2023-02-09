class User_node:
    def __init__(self, user_name: str, genre_nodes: list = None):
        self.user_name = user_name
        if genre_nodes is not None:
            self.genre_nodes = genre_nodes
        else:
            self.genre_nodes = []
    
    def __str__(self):
        return "User name is "+ str(self.user_name)
    
    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return len(self.genre_nodes)