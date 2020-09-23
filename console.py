import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo

artist_1 = Artist('Michael', 'Jackson')
print(artist_1.__dict__)
artist_repo.save(artist_1)

artist_2 = Artist('Bullet for ', 'my Valentine')
print(artist_2.__dict__)
artist_repo.save(artist_2)

artist_3 = Artist('Britney', 'Spears')
print(artist_3.__dict__)
artist_repo.save(artist_3)

album_1 = Album('Thriller', 'Pop', artist_1)
print(album_1.__dict__)
album_repo.save(album_1)

album_2 = Album('Fever', 'Emo', artist_2)
print(album_2.__dict__)
album_repo.save(album_2)

album_3 = Album ('In the Zone', 'Pop', artist_3)
print(album_3.__dict__)
album_repo.save(album_3)

pdb.set_trace()