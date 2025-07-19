# Generate bg_music.wav (simple looping music)
def generate_background_music(filename, duration=8, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave1 = np.sin(2 * np.pi * 440 * t)  # A4
    wave2 = np.sin(2 * np.pi * 660 * t)  # E5
    music = ((wave1 + wave2) * 0.3 * 32767).astype(np.int16)
    with wave.open(filename, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        f.writeframes(music.tobytes())

generate_background_music("assets/bg_music.wav")
