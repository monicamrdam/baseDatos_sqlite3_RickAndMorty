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
    def __init__(self, name: str, popularity: int):
        self.name = name
        self.popularity = popularity