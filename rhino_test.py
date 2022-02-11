import pvrhino
import pyaudio
import struct
import config
access_key = config.access_key
context_path = config.context_path

handle = pvrhino.create(access_key=access_key, context_path=context_path)

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