import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("i am vazu , and i am your assistent")

def grretme():
    h=int(datetime.datetime.now().hour)
    if h>0 and h<=12:
        speak("good morning")
    elif h>12  and h<=18:
        speak("good afternoon")
    else:
        speak("good evening")
# print(grretme())

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
    # with sr.Microphone() as source:
        print("listening...")
        speak("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
       print("recogninzing....")
       speak("recognizing...")
       query=r.recognize_google(audio,language='en-in')
       print(f"user said={query}\n")

    except Exception  as e:
        speak("say that again please...")
        return "none"
    return query
if __name__ == "__main__":
 grretme()
 while True:
  query= takeCommand().lower()
  if'wikipedia' in query:
      speak("searching wikipedia")
      query=query.replace("wikipedia","")
      results=wikipedia.summary(query,sentences=5)
      print(results)
      speak(results)

  # elif 'open youtube' in query:
  #      # webbrowser.open("youtube.com")
  #      webbrowser.open("youtube.com")
  elif 'open youtube' in query:
      webbrowser.open("youtube.com")
  elif 'open hello' in query:
      webbrowser.open("chat.openai.com")
  elif 'happy' in query:
      speak("happy birthday sayyad bhai,")
      music_dir="C:\\Users\Asus\Desktop\music\01-Monk-Turner-Fascinoma-Its-Your-Birthday (1).mp3"
      songs=os.listdir(music_dir)
      print(songs)
      os.startfile(os.path.join(music_dir, songs[1]))