import speech_recognition as sr
import pyaudio
    
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
 
name=["Abhinav","Animesh","monu","mom","Mom"]
"""response = 'n'

print("Welcome to Our New App")
print("What do people call you?")
name.append(input())
while True:
    print("Do you want to add another name? (y/n) :")
    response=input()
    if response =='y':
        print("Enter name:")
        name.append(input())
    else :
        break"""
        
print("Your names are:")
print(name)
#-------------------------------------------------------------------------------------------------------------
def recognize_speech_from_mic(recognizer, microphone):
     # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        #print(audio)

    # set up the response object
    response = {"success": True,"error": None,"transcription": None}

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response
#--------------------------------------------------------------------------------------------------------------------

recognizer = sr.Recognizer()
microphone = sr.Microphone()

guess = recognize_speech_from_mic(recognizer, microphone)
print (guess["transcription"])
for x in name:
    if guess["transcription"] == x:
        print("Someone called your name..Stop System Sound")
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # Control volume
        #volume.SetMasterVolumeLevel(-0.0, None) #max
        #volume.SetMasterVolumeLevel(-5.0, None) #72%
        volume.SetMasterVolumeLevel(-20.0, None) #51%
        break
    


   
    
    