from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (name, artist_id) VALUES (%s, %s) RETURNING *"
    values = [album.name, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album

def select_all_albums():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for result in results:
        artist = artist_repository.select(result["artist_id"])
        album = Album(result["name"], artist, result["id"])
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result["artist_id"])
        album = Album(result["name"], artist, result["id"])
    return album


def delete_album(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all_albums():
    sql = "DELETE FROM albums"
    run_sql(sql)

def update(album):
    sql = "UPDATE album SET (name, artist) = (%s, %s) WHERE id = %s"
    values = [album.name, album.artist, album.id]
    run_sql(sql, values)

def edit_album_name(album, new_name):
    sql = "UPDATE albums SET name = %s WHERE id = %s"
    values = [new_name, album.id]
    run_sql(sql, values)