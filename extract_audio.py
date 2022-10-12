import moviepy
import moviepy.editor


def extract_audio_from_video(path):
    video = moviepy.editor.VideoFileClip(path)   

    # Convert video to audio
    audio = video.audio
    audio.write_audiofile('finalaudio.mp3')

if __name__=="__main__":
    path = r"" #put your video file path here
    extract_audio_from_video(path)