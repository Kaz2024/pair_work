from lib.pair_test_drive_class import *

def test_the_musictrack_name(): #TRACKNAME
    musicTrack = MusicTrack("Liked Songs")
    actual = musicTrack.name
    assert actual == "Liked Songs"

def test_add_songs():#Addsongs
    musicTrack= MusicTrack("Liked Songs")
    musicTrack.add_song("Baby")
    assert musicTrack.songlist == ["Baby"]

def test_the_content_of_the_list(): #Display lists of songs
    musicTrack= MusicTrack("Liked Songs")
    musicTrack.add_song("Baby")
    musicTrack.add_song("Circle of life")
    assert musicTrack.see_contents() ==["Baby", "Circle of life"]