from pyaudio import PyAudio
"""
Returns a list of the names of all available microphones. For microphones where the name can't be retrieved, the list entry contains ``None`` instead.

The index of each microphone's name is the same as its device index when creating a ``Microphone`` instance - indices in this list can be used as values of ``device_index``.
"""
audio = PyAudio()
try:
    for i in range(audio.get_device_count()):
        device_info = audio.get_device_info_by_index(i)
        print(device_info.get("name"))
finally:
    audio.terminate()
