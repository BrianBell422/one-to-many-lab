import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

from models.artist import Artist
from models.album import Album

import pdb

album_repository.delete_all_albums()
artist_repository.delete_all_artists()

artist_1 = Artist("fred", "davis")
album_1 = Album("Purple Rain", artist_1)

artist_repository.save(artist_1)
# print(artist_repository.select_all_artists()[0].first_name)

album_repository.save(album_1)

# album_repository.delete_album(album_1.id)
# artist_repository.delete_artist(artist_1.id)

# print(artist_repository.list_albums(artist_1)[0].name)

# artist_2 = Artist("Prince", "")
artist_repository.edit_artist_first_name(artist_1, "Peter")
# print(artist_repository.select_all_artists()[0].first_name)

album_repository.edit_album_name(album_1, "Black snow")
print(album_repository.select_all_albums()[0].name)