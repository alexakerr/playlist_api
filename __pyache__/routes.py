from app import app
from flask import request
from .manager import PlaylistManager

playlist_manager = PlaylistManager()


@app.route('/playlist/create', methods=['POST'])
def create_playlist():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description', "")
    playlist_id = playlist_manager.create_playlist(name, description)
    return {'playlist_id': playlist_id}, 201




@app.route('/playlist/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    playlist = playlist_manager.get_playlist(playlist_id)
    if playlist:
        return playlist
    else:
        return {'error': 'Playlist not found.'}, 404




@app.route('/playlist/update/<int:playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    playlist_manager.update_playlist(playlist_id, name, description)
    return {'message': 'Playlist has been updated successfully!'}




@app.route('/playlist/delete/<int:playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    playlist_manager.delete_playlist(playlist_id)
    return {'message': 'Playlist has been successfully deleted!'}





@app.route('/playlist/<int:playlist_id>/add_song', methods=['POST'])
def add_song_to_playlist(playlist_id):
    data = request.get_json()
    song_id = data.get('song_id')
    playlist_manager.add_song_to_playlist(playlist_id, song_id)
    return {'message': 'Song added to playlist successfully!'}




@app.route('/playlist/<int:playlist_id>/remove_song/<int:song_id>', methods=['DELETE'])
def remove_song_from_playlist(playlist_id, song_id):
    playlist_manager.remove_song_from_playlist(playlist_id, song_id)
    return {'message': 'Song has been removed from the playlist successfully'}




@app.route('/playlist/search', methods=['GET'])
def search_song():
    query = request.args.get('query')
    results = playlist_manager.search_song(query)
    return results


if __name__ == '__main__':
    app.run(debug=True)