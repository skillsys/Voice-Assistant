from asyncio.windows_events import ERROR_CONNECTION_REFUSED
import struct
import pyaudio
import pvporcupine
from config import access_key

porcupine = None
pa = None
audio_stream = None


sen = [0.5]


try:
    porcupine = pvporcupine.create(access_key=access_key , keyword_paths=['./Ai_models\\hey-sam_en_windows.ppn'] , sensitivities=sen)

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("Hotword Detected")
except ERROR_CONNECTION_REFUSED:
    pass
print(1)