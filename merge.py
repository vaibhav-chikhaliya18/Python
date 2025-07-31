from pydub import AudioSegment

# Set FFmpeg paths (if needed)
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"

# Load two audio files
audio1 = AudioSegment.from_file(r"sound1.mp3")
audio2 = AudioSegment.from_file(r"hello.mp3")

# Concatenate
merged = audio1 + audio2

# Export merged file
merged.export(r"E:\python\temp_audio\merged_concat.mp3", format="mp3")

print("✅ Audio merged (concatenated) successfully!")
