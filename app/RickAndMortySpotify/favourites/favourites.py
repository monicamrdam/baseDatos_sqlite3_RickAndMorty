class Favourites:
    def __init__(self, name: str, popularity: int, popularTracks):
        self.name = name
        self.popularity = popularity
        self.popularTracks = []

    def __str__(self):
        return "Name: {}, Popularity: {}, PopularTracks: {}".format(
            self.name, self.popularity, self.popularTracks
        )

    def serialize(self):
        return {
            'Name': self.name,
            'Popularity': self.popularity,
            'PopularTracks': self.popularTracks,
        }
