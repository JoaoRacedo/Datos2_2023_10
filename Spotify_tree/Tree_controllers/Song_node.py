class Song_node:
    def __init__(self, song_name: str, artist_name: str):
        self.song_name = song_name
        self.artist_name = artist_name
    
    def __str__(self):
        return "Song name is "+ str(self.song_name) + " and the artist is " + str(self.artist_name)
    
    def __repr__(self):
        return str(self)