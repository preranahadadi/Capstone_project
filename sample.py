import vlc
import time

vlc_instance = vlc.Instance()
     
# creating a media player
player = vlc_instance.media_player_new()

# creating a media
media = vlc_instance.media_new(r"C:\Users\bilva\Decypher\video\american3.mp4")

# setting media to the player
player.set_media(media)
duration = player.get_length()
# play the video
player.play()

