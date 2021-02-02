from models.artist import Artist

from db.run_sql import run_sql

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