# Voice-Assistant
A Voice assistant that is completely local and runs your machine

Sam(Semi-Automatic-Machine) is a prototype open source voice assistant able to automate different tasks and engage in simple conversations.

------
## Running on native machine
### dependencies
* python3
* pip


If you're on mac or linux you can install `pyaudio` using `pip install PyAudio`

**NOTICE: If you are using windows installing pyaudio is using pip is broken from python 3.6 and above. to install pyaudio you can use the whl file included in project**


### using virtualenv (recommend) (optional)
1. `python -m venv voiceAssistantenv`
2. `cd voiceAssistantenv\scripts\`
2. `.\activate`

### pip packages
`cd Voice-Assistant`

`pip install -r requirements.txt` 

### pyaudio install for windows users
1. `cd Voice-Assistant`
2. `pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl`

To run the assistant you need to create an account at [picovoice website](https://console.picovoice.ai/) and get and access key from the console but after that the Assistant entirely runs offline on your system.
----
Create a config.py file and 


### Running the assistant
* `python main_assistant.py`
----

**NOTE: if your voice is not detected then please check if correct microphone is selected you can run `python microphone_lister.py` to get the list of microphones**



**please raise an issue if your are facing any problems.**

(all commands can be uttered in any combination as we are using a speech to intent system)


## (new commands comming soon)

>supported commands: (All commmands
support different uttrances check yaml files of rhino for extra details)




1. what's the time
1. what's the date
1. 

