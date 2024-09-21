def on_forever():
    pass
basic.forever(on_forever)
music.play(music.string_playable("", 120), music.PlaybackMode.UNTIL_DONE)