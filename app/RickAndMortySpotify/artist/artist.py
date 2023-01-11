class Artist:
    def __init__(self, name: str, popularity: int):
        self.name = name
        self.popularity = popularity

    def __str__(self):
        return "Name: {}, Popularity: {}".format(
           self.name, self.popularity
         )

    def serialize(self):
        return {
        'Name': self.name,
        'Popularity': self.popularity,}


class TopTracks:
    def __init__(self, name_song: str, popularity: int):
        self.name_song = name_song
        self.popularity = popularity

    def __str__(self):
        return "Name_song: {}, Popularity: {}".format(
           self.name_song, self.popularity
         )

    def serialize(self):
        return {
        'Name_song': self.name_song,
        'Popularity': self.popularity,}