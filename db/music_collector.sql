DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists(
    id SERIAL PRIMARY KEY, 
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

CREATE TABLE albums(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255) NOT NULL,
    artist_id INT REFERENCES artists(id)
);