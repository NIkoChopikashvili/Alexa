import speech_recognition as sr
import webbrowser
import time
import playsound
import random
import os 
from time import ctime
from gtts import gTTS

recog = sr.Recognizer()
def record_audio(ask = False):
  with sr.Microphone() as source:
    if ask:
      alexa_speak(ask)
    audio = recog.listen(source)
    text = ''
    try:
      text = recog.recognize_google(audio)
    except sr.UnknownValueError:
      alexa_speak('sorry could not recognize your voice, try again')
    except sr.RequestError:
      alexa_speak("sorry, my service isnt working")

def alexa_speak(audio_string):
  tts = gTTS(text=audio_string, lang='en')
  r = random.randint(1, 10000000)
  audio_file = 'audio-' + str(r) + '.mp3'
  tts.save(audio_file)
  playsound.playsound(audio_file)
  print(audio_string)
  os.remove(audio_file)

def respond(text):
  if 'how is the traffic today' in text:
    webbrowser.get().open('https://www.google.com/search?q=tbilisi+traffic&rlz=1C1GCEA_enGE832GE832&oq=tbilisi+traff&aqs=chrome.0.0j0i457j69i57j0j0i22i30l3.7713j0j7&sourceid=chrome&ie=UTF-8')
  if 'good morning alexa' in text:
    alexa_speak('Good morning sir')
  if 'how are you' in text:
    alexa_speak('good, how are you?')
  if 'what is the weather in tbilisi' in text:
    weather_url = 'https://www.google.com/search?source=hp&ei=CNc8YI_BNdXggwedqpfgBA&iflsig=AINFCbYAAAAAYDzlGInwbZhFbKoDWMc_s8u3fyy3zrC0&q=what%27s+the+weather+in+tbilisi&oq=whats+the+weather+in+tb&gs_lcp=Cgdnd3Mtd2l6EAMYADIECAAQDTIGCAAQFhAeMgsIABDJAxAWEAoQHjIGCAAQFhAeOggIABCxAxCDAToCCAA6BQgAELEDOgsILhCxAxDHARCvAToICC4QsQMQgwE6AgguOgUILhCxAzoECAAQCjoFCAAQyQM6BwgAEEYQgAJQ2BBYpURgpkpoAnAAeACAAfEBiAHSHJIBBjAuMjMuMZgBAKABAaoBB2d3cy13aXqwAQA&sclient=gws-wiz'
    webbrowser.get().open(weather_url)
  if 'what is your name' in text:
    alexa_speak('My name is Alexa')
  if 'Alexa show me date' in text:
    alexa_speak(ctime())
  if 'what time is it' in text:
    alexa_speak(ctime())
  if 'search' in text:
    search = record_audio('what do you want to search for?')
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    alexa_speak('here is what i found for' + search)
  if 'find location' in text:
    location = record_audio('what location do you want to search for?')
    url = 'https://google.nl/maps/place/' + location + '/&amp;'
    webbrowser.get().open(url)
    alexa_speak('here is location of' + location)
  if 'exit' in text:
    exit()

time.sleep(1)
alexa_speak("Is there anything i can help u with?")
while 1:
  text = record_audio()
  respond(text)