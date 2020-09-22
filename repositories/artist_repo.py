from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

def save(artist):
    sql = f"INSERT INTO artists (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [artist.first_name, artist.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select(artist):
    artist = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = artist.select(result['artist_id'])
        task = Artist(result["first_name"], result["last_name"])
    return artist

def select_all():
    artists = []

    sql = "SELECT * FROM artist"
    results = run_sql(sql)

    for row in results:
        artist = artist.select(row['user_id'])
        artist = Artist(row["first_name"], ["last_name"])
        artists.append(artist)
    return artist

def albums(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id=%s"
    values = [artist.id]
    results = run_sql(sql, values)
    for row in results:
        album = Album(row["name"], row["genre"], artist, row["id"])
        albums.append(album)
    return albums
