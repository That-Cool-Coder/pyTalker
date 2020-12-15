import pyttsx3
import speech_recognition
import errors
import chatbot
import simpleFileManager as files
import json

#INTRODUCTION_SENTENCE = 'Hi, I\'m a chatbot! Say something and I will reply'
INTRODUCTION_SENTENCE = 'Hi! Say something'
SENTENCE_NOT_UNDERSTOOD = 'Sorry, I didn\'t userstand that (speak more clearly, idiot!)'
CONFIG_FILE_NAME = 'config.json'

CONFIG = {}

# Speech to text engine stuff
# ---------------------------

speechRecogniser = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()

def getSentenceInput():
    with microphone as source:
        speechRecogniser.adjust_for_ambient_noise(source)
        audio = speechRecogniser.listen(source)
    
    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = speechRecogniser.recognize_google(audio)
    except speechRecogniser.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except speechRecogniser.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    
    return response

# TTS Engine stuff
# ----------------

ttsEngine = pyttsx3.init()

def setTtsVoice(voiceIdx, catchError=False):

    # get the voice list
    voices = ttsEngine.getProperty('voices')

    # If there are no voices, raise an error
    if len(voices) == 0:
        raise NoVoicesFoundError

    # Try to set the voice at the index
    try:
        ttsEngine.setProperty(voices[voiceIdx].id)
    except IndexError:
        # If the voice can't be found, then either raise an error or...
        # ...use the first voice in the list.
        # There can't be no voices in the list as there is a checker in the if above
        if catchError:
            ttsEngine.setProperty(voices[0].id)
        else:
            raise IndexError

def sayNow(words):
    ttsEngine.say(words)
    ttsEngine.runAndWait()

# Config
# ------

def loadConfig():
    global CONFIG

    # Attempt to read the config from the file
    try:
        rawFile = files.read(CONFIG_FILE_NAME)
    except:
        print('Error reading config file (' + CONFIG_FILE_NAME + ')')
        input('Press enter to close')
        quit()

    # Attempt to parse the config
    try:
        CONFIG = json.loads(rawFile)
    except:
        print('Error parsing config file (' + CONFIG_FILE_NAME + ')')
        input('Press enter to close')
        quit()
    
    # Use the config to setup text to speech
    for key in CONFIG['textToSpeech'].keys():
        try:
            # Because voice setting just had to be different from the others
            if key == 'voice':
                setTtsVoice(CONFIG['textToSpeech'][key])
            else:
                ttsEngine.setProperty(key, CONFIG['textToSpeech'][key])
        except:
            print('Error: no property with name ' + key)
            input('Press enter to close')
            quit()

# Main loop, driver
# -----------------

def mainLoop():
    while True:
        response = getSentenceInput()
        if response['success']:
            userInput = response['transcription']
            print(userInput)
            reply = chatbot.replyToSentence(userInput)
            print(reply)
            sayNow(reply)
        else:
            print(SENTENCE_NOT_UNDERSTOOD)
            sayNow(SENTENCE_NOT_UNDERSTOOD)

if __name__ == '__main__':
    try:
        loadConfig()
    except:
        print('Warning: error loading config')
        input()
        
    print(INTRODUCTION_SENTENCE)
    sayNow(INTRODUCTION_SENTENCE)
    mainLoop()
