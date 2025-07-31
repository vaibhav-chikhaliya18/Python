
# import os
# import tempfile
# from pydub import AudioSegment
# from pydub.playback import play

# # Set FFmpeg paths
# AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
# AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"

# # Use Python default temp folder
# tempfile.tempdir = None  # Let Python handle the temp dir

# # Load the audio file
# audio_file = "sound1.mp3"  # change to your file
# sound = AudioSegment.from_file(audio_file)

# # Play the audio
# print("Playing audio...")
# play(sound)
# print("Playback finished!")



from playsound import playsound

audio_file = r"audio1.mp3"  # change to your file
print("Playing audio...")
playsound(audio_file)
print("Playback finished!")