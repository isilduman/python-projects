def sing_song():
    print("and if you'd never come for me")
    print("I might've drowned in the melancholy")
    print("I swore my loyalty to me, myself and I")
    print("Right before you lit my sky up")
sing_song()
def sing(song_name, lyrics):
    print("🎵 Now playing:", song_name)
    print(lyrics)
sing("The Fate of Ophelia","""All that time
I sat alone in my tower
You were just honing your powers
Now I can see it all (see it all)
Late one night
You dug me out of my grave and
Saved my heart from the fate of
Ophelia""")
def repeating_lyrics(line,times):
    for i in range(times):
        print(line)
repeating_lyrics("""You dug me out of my grave and
Saved my heart from the fate of
Ophelia""",2)