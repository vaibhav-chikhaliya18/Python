import os
from pydub import AudioSegment

# Set FFmpeg paths
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"

# Paths
audio_file = r"E:\python\sound1.mp3"
temp_wav = r"E:\python\temp_audio\temp_sound.wav"

# Load and export audio
sound = AudioSegment.from_file(audio_file)
sound.export(temp_wav, format="wav")

# Play using ffplay (blocking until finished)
print("Playing audio...")
os.system(f'"C:\\ffmpeg\\bin\\ffplay.exe" -nodisp -autoexit "{temp_wav}"')
print("Playback finished!")