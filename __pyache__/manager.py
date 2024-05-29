class PlaylistManager:
    def __init__(self):
        self.playlists = {}
        self.songs = {}
        self.user_preferences = {}


    def create_playlist(self, name, description=""):
        playlist_id = len(self.playlists) + 1
        self.playlists[playlist_id] = {'name': name, 'description': description, 'songs': []}
        return playlist_id
    

    def get_playlist(self, playlist_id):
        if playlist_id in self.playlists:
            return self.playlists[playlist_id]
        else:
            return None
         

    def update_playlist(self, playlist_id, name=None, description=None):
        if playlist_id in self.playlists:
            if name:
                self.playlists[playlist_id]['name'] = name
            if description:
                self.playlists[playlist_id]['description'] = description
        else:
            return None
            


    def delete_playlist(self, playlist_id):
        if playlist_id in self.playlists:
            del self.playlists[playlist_id] 
        else:
            return None  


    def add_song_to_playlist(self, playlist_id, song_id):
        if playlist_id in self.playlists and song_id in self.songs:
            self.playlists[playlist_id]['songs'].append(song_id)
        else:
            return None


    def remove_song_from_playlist(self, playlist_id, song_id):
        if playlist_id in self.playlists and song_id in self.songs:
            self.playlists[playlist_id]['songs'].remove(song_id)
        else:
            return None


    def search_song(self, query):
        results = []
        for song_id, song_details in self.songs.items():
            if query.lower() in song_details['title'].lower() or query.lower() in song_details['artist'].lower():
                results.append(song_details)
        return results
    

