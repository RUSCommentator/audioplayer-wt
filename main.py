import pytube as pt
import vlc

def zxc(url):
    player = vlc.MediaPlayer(url)
    player.play()
    input("Playing audio. Press any key to stop.")
    player.stop()

def audioxoxol(url):
    yt = pt.YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download()
    audio_file_path = audio.default_filename
    play_audio(audio_file_path)

if __name__ == '__main__':
    video_url = input("Enter URL: ")
    audioxoxol(video_url)
