import pvporcupine
import pvrhino
import struct
import pyaudio
import pyttsx3
import whatis_module
from config import access_key

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
print(engine.getProperty('rate'))
engine.setProperty('voice', voices[1].id )
engine.setProperty('rate' , 195)

whatis = whatis_module.whatis()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()





rhino = pvrhino.create(access_key=access_key, context_path=".\\Ai_models\\dateTime_en_windows.rhn")
porcupine = pvporcupine.create(access_key=access_key , keyword_paths=['.\\Ai_models\\hey-sam_en_windows.ppn'])
pa = pyaudio.PyAudio()

assert porcupine.sample_rate == rhino.sample_rate
sample_rate = porcupine.sample_rate

assert porcupine.frame_length == rhino.frame_length
frame_length = porcupine.frame_length

audio_stream = pa.open(
                rate=sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=frame_length)

wkd = False
while True:
    pcm = audio_stream.read(frame_length)
    audio_frame = struct.unpack_from("h" * frame_length, pcm)

    
    if not wkd:
        keyword_index = porcupine.process(audio_frame)
        if keyword_index >= 0:
            print("Hotword Detected")
            wkd = True
    else: 
        is_finalized = rhino.process(audio_frame)
        print(is_finalized)
        if is_finalized:
            inference = rhino.get_inference()
            wkd = False
            if not inference.is_understood:
                # add code to rhino unsupported commands
                pass
            else:
                intent = inference.intent
                slots = inference.slots
                print(type(intent))
                speak(whatis.process(slots["TD"]))
                


        

