from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repo as artist_repo

def save(album):
    sql = "INSERT INTO albums (name, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repo.select(row['artist_id'])
        album = Album(row['name'], row['genre'], row['id'], artist)
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = artist_repo.select(result['artist_id'])
        album = Album(result["name"], result["genre"], artist, result["id"])
    return album

def artist(id):
    artist = None
    album = select(id)
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [albums.artist.id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result["first_name"], result["last_name"], result["id"])
    return artist




