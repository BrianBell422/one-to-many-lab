import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

from models.artist import Artist
from models.album import Album

import pdb


artist_1 = Artist("fred", "davis")

artist_repository.save(artist_1)
print(artist_repository.select_all_artists()[0].first_name)

