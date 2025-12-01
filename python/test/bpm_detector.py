import librosa

# ===== MP3ファイルを読み込む =====
filename = "your_song.mp3"
y, sr = librosa.load(filename, sr=None, mono=True)

# ===== オンセット強度（打楽器的変化）を取得 =====
onset_env = librosa.onset.onset_strength(y=y, sr=sr)

# ===== テンポ推定 =====
tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)

print(f"Estimated BPM: {tempo:.2f}")
