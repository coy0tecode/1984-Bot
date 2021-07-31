import speech_recognition as sr
import pyttsx3
from os import path
import wave




# Test functionality by playing back text
# Not used in the bot, just for testing
def replay(text):
    engine = pyttsx3.init(driverName='sapi5', debug=False)
    engine.say(text)
    engine.runAndWait()
    
# Function for inifinite loop to listen, convert, and play back speech
# Not used in the bot, just for testing
def mic_test():
    while True:
        try:
            with sr.Microphone() as source:
                r = sr.Recognizer()
                r.adjust_for_ambient_noise(source, duration=0.5)
            
                audio = r.listen(source)
            
                text = r.recognize_google(audio)
                text = text.lower()
            
                print("I heard..." + text)
                replay(text)
                
        except sr.RequestError as e:
            print(f"Error requesting results; {e}")
        
        except sr.UnknownValueError:
            print("Unrecognized audio")
        
        
# Function to write raw file as wav, get text from audio file
def from_audio_file():
    r = sr.Recognizer()
    audio_file = path.join(path.dirname(path.realpath(__file__)), "audio")
    
    with open(audio_file, 'rb') as pcmfile:
        pcmdata = pcmfile.read()
        
    with wave.open(audio_file + '.wav', 'wb') as wavfile:
        wavfile.setparams((2, 2, 44100, 0, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)
        
    wave_audio_file = path.join(path.dirname(path.realpath(__file__)), "audio.wav")
    
    with sr.AudioFile(wave_audio_file) as source:
        audio = r.record(source)
        
    try:
        text = r.recognize_google(audio)
        text = text.lower()
        print(text)
        return text
        
    except sr.RequestError as e:
        print(f"Error requesting results; {e}")
    
    except sr.UnknownValueError:
        print("Unrecgonized audio")