import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify_Stuff:
    """
    A class to represent spotify API and interactions.
    
    ...
    Attributes
    ----------
    None
    Methods
    -------
    get_id(spotify_url : str =):
        Returns the spotify id given a spotify URL
    
    def get_user(self, spotify_user_id: str = None):
        Returns the spotify user info given a spotify user id

    def get_artist_genre(self, spotify_artist_id: str = None):
        Returns the spotify artist genre given a spotify artist id
    
    def get_artist_genre(self, spotify_artist_id: str = None):
        Returns the spotify artist genre given a spotify artist id
    
    def get_playlist_items_by_id(self, id_playlist : str = None):
        Returns list with the information of the playlist.
    """

    def __init__(self):
        """
        Constructs the spotify object given the credentials
        Parameters
        ----------
        None
        """
        client_credentials_manager = SpotifyClientCredentials(
            "SPOTIPY_CLIENT_ID", \
            "SPOTIPY_CLIENT_SECRET")
        self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    def get_id(self, spotify_url : str = None):
        """
        Returns the spotify id given a spotify URL
        Parameters
        ----------
        spotify_url : str. If not provided an error is raise
            Spotify URL
        
        Returns
        -------
        Spotify ID of URL
        """
        if spotify_url is None:
            raise TypeError("URL needed")
        spotify_id = spotify_url.split("/")[-1].split("?")[0]
        return spotify_id
    
    def get_user(self, spotify_user_id: str = None):
        """
        Returns the spotify user info given a spotify user id

        Parameters
        ----------
        spotify_user_id : str. If not provided an error is raise
            Spotify user id

        Returns
        -------
        Spotify user info
        """
        user_id = spotify_user_id.split(":")[-1]
        user_info = self.spotify.user(user_id)
        return user_info["display_name"]
    
    def get_artist_genre(self, spotify_artist_id: str = None):
        """
        Returns the spotify artist genre given a spotify artist id

        Parameters
        ----------
        spotify_artist_id : str. If not provided an error is raise
            Spotify artist id

        Returns
        -------
        Spotify artist genre
        """
        artist_info = self.spotify.artist(spotify_artist_id)
        artist_info = artist_info["genres"]
        return artist_info

    def get_playlist_items_by_id(self, id_playlist : str = None):
        """
        Returns list with the information of the playlist.
        lista[0] is string with user name that added track that is in list[2]
        lista[1] is string with band name
        lista[2] is a string with track name
        lista[3] is a list with band genres 
        Parameters
        ----------
            id_playlist : str. playlist id
        
        Returns
        -------
        list with the information of the playlist
        """
        if id_playlist is None:
            url_playlist = "https://open.spotify.com/playlist/7y1yhwfkpWxUNH7K2TUY4X?si=kasgGVgtR-KEOaSZnzzH_g"
            id_playlist = self.get_id(url_playlist)

        results = self.spotify.playlist_items(id_playlist)
        lista = []
        for track in results["items"]:
            user_id = track["added_by"]["uri"]
            user_relevant_info = self.get_user(user_id)
            artist_name = track["track"]["artists"][0]["name"]
            artist_id = track["track"]["artists"][0]["external_urls"]["spotify"]
            artist_genre = self.get_artist_genre(artist_id)
            track_added = track["track"]["name"]
            lista.append([user_relevant_info, artist_name, track_added, artist_genre])
    
        return lista
    
