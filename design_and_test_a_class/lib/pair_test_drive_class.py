class MusicTrack():
    def __init__(self,name):
        self.name = name
        self.songlist= []

    def add_song(self, song):
        self.songlist.append(song)

    def see_contents(self):
        return self.songlist 