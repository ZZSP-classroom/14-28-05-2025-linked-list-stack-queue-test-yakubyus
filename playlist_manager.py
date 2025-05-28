class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if self.head is None:
            self.head = new_song
            return
        current_song = self.head
        while current_song.next:
            current_song = current_song.next
        current_song.next = new_song

    def remove_song(self):
        if self.head is None:
            return
        self.head = self.head.next

    def get_next_song(self):
        if self.head:
            return self.head.title, self.head.artist
        return None, None
