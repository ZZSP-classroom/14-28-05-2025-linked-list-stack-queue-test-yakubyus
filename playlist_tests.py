import unittest
from playlist_manager import LinkedList


class TestPlaylistManager(unittest.TestCase):
    def test_add_song(self):
        playlist = LinkedList()
        playlist.add_song("Shape of You", "Ed Sheeran")
        self.assertEqual(playlist.get_next_song(), ("Shape of You", "Ed Sheeran"))

    def test_remove_song(self):
        playlist = LinkedList()
        playlist.add_song("Shape of You", "Ed Sheeran")
        playlist.add_song("Blinding Lights", "The Weeknd")
        playlist.remove_song()
        self.assertEqual(playlist.get_next_song(), ("Blinding Lights", "The Weeknd"))

    def test_get_next_song(self):
        playlist = LinkedList()
        playlist.add_song("Shape of You", "Ed Sheeran")
        playlist.add_song("Blinding Lights", "The Weeknd")
        self.assertEqual(playlist.get_next_song(), ("Shape of You", "Ed Sheeran"))


if __name__ == '__main__':
    unittest.main()
