from models.artist import Artist
from models.album import Album

from db.run_sql import run_sql

import repositories.artist_repository as artist_repository

def save(artist):
    sql  = "INSERT INTO artists (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [artist.first_name, artist.last_name]
    results = run_sql(sql, values)

    id = results[0]["id"]
    artist.id = id

    return artist
    

def select_all_artists():
    artists =[]
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    
    for result in results:
        artist = Artist(result["first_name"], result["last_name"], result["id"])
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        artist = Artist(results["first_name"], results["last_name"], results["id"])
    return artist

def delete_artist(id):
    sql = "DELETE FROM artists WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def delete_all_artists():
    sql = "DELETE FROM artists"
    run_sql(sql)

def list_albums(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id=%s"
    values = [artist.id]
    results = run_sql(sql, values)

    for result in results:
        artist = artist_repository.select(result["artist_id"])
        album = Album(result["name"], artist, result["id"])
        albums.append(album)
    return albums

def update(artist):
    sql = "UPDATE artists SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [artist.first_name, artist.last_name, artist.id]
    run_sql(sql, values)


def edit_artist_first_name(artist, new_first_name):
    sql = "UPDATE artists SET first_name = %s WHERE id = %s"
    values  = [new_first_name, artist.id]
    run_sql(sql, values)

