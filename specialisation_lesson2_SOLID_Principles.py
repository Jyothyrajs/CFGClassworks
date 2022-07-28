class Album:

    def __init__(self, name, artist, songs) -> None:
        self.name = name
        self.artist = artist
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    # breaks the SRP !!!
    def search_album_by_artist(self):
        """ Searching the database for other albums by same artist """
        pass

# INSTEAD CREATE ANOTHER CLASS

class AlbumBrowser:
    """ Class for browsing the Albums database"""

    def search_album_by_artist(self, albums, artist):
        pass

    def search_album_starting_with_letter(self, albums, letter):
        pass


"""
OPEN-CLOSED PRINCIPLE

Classes, modules, functions, etc. should be open for extension, but closed for modification.
"""

# BEFORE


class AlbumBrowser:

    def search_album_by_artist(self, albums, artist):
        return [album for album in albums if album.artist == artist]

    def search_album_by_genre(self, albums, genre):
        return [album for album in albums if album.genre == genre]



# Now what happens if we want to search by artist or by genre?
    # What if we add release year?
    # We will have to write a new function every time modifying the class!
    # combination of 4 elements -> 16 different functions


# INSTEAD

class SearchBy:
    def is_matched(self, album):
        pass


class SearchByGenre(SearchBy):
    def __init__(self, genre):
        self.genre = genre

    def is_matched(self, album):
        return album.genre == self.genre


class SearchByArtist(SearchBy):
    def __init__(self, artist):
        self.artist = artist

    def is_matched(self, album):
        return album.artist == self.artist


class AlbumBrowser:

    # Note we pass one of the classes as searchby arg
    def browse(self, albums, searchby):
        return [album for album in albums if searchby.is_matched(album)]


"""
INTERFACE SEGREGATION PRINCIPLE

"Clients should not be forced to depend upon interfaces that they do not use."
"""

class PlaySongs:

    def __init__(self, title):
        self.title = title

    def play_drums(self):
        print("Bum-bum-bum")

    def play_guitar(self):
        print("Some guitar solo*")
    # Better to remove as lyrics is not there for all songs
    def sing_lyrics(self):
        print("Lalalalala")



class PlayRockSongs(PlaySongs):

    def play_guitar(self):
        print("Heavy metal guitar solo*")

    def sing_lyrics(self):
        print("We will, we will rock you!")



class PlayInstrumentalSongs(PlaySongs):
    def sing_lyrics(self):
        raise Exception("No lyrics for instrumental songs")


# INSTEAD

from abc import abstractmethod


class PlaySongsLyrics:

    @abstractmethod
    def sing_lyrics(self):
        pass


class PlaySongsMusic:

    @abstractmethod
    def play_guitar(self):
        pass

    @abstractmethod
    def play_drums(self):
        pass


class PlayInstrumentalSong(PlaySongsMusic):

    def play_drums(self):
        print("Bum-bum-bum")

    def play_guitar(self):
        print("Some guitar solo*")


class PlayRockSong(PlaySongsMusic, PlaySongsLyrics):

    def play_guitar(self):
        print("Heavy metal guitar solo*")

    def sing_lyrics(self):
        print("We will, we will rock you")

    def play_drums(self):
        print("Bum-bum-bum")

# IMPORTANT
    # ViewRockAlbums explicitly depends on the fact that albums are stored in a tuple in a certain order inside AlbumShop.
    # It should have no knowledge of the internal structure of AlbumShop.
    # Now if we change the ordering in the tuples in the album, our code would break.


# INSTEAD

class GeneralAlbumShop:
    """Thi menthokgdhfghcc"""
    @abstractmethod
    def filter_by_genre(self, genre):
        pass


class MyAlbumShop(GeneralAlbumShop):
    albums = []

    def add_album(self, name, artist, genre):
        self.albums.append((name, artist, genre))

    def filter_by_genre(self, genre):
        for album in self.albums:
            if album[2] == genre:
                yield album[0]


class ViewRockAlbums:
    def __init__(self, album_store):
        for album_name in album_store.filter_by_genre("Rock"):
            print("We have {} in our shop.".format(album_name))

    # NOTE: if we had another type of AlbumShop, that decides to store the album differently,
    # it would need to implement the same interface for filter_by_genre to make ViewRockAlbums work.