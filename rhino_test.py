import pvrhino
import pyaudio
import struct
from config import access_key



handle = pvrhino.create(access_key=access_key, context_path=".\\Ai_models\\dateTime_en_windows.rhn")

pa = pyaudio.PyAudio()

audio_stream = pa.open(
                rate=handle.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=handle.frame_length)
while True:
    pcm = audio_stream.read(handle.frame_length)
    pcm = struct.unpack_from("h" * handle.frame_length, pcm)

    
    is_finalized = handle.process(pcm)

    if is_finalized:
        inference = handle.get_inference()
        if not inference.is_understood:
            # add code to handle unsupported commands
            pass
        else:
            intent = inference.intent
            slots = inference.slots
            print(intent)