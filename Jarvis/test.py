import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for idx,voice in enumerate(voices):
    if voice.languages[0] == 'en_US':
        print(idx,voice, voice.id)
        engine.setProperty('voice', voice.id)
        engine.say("Hi")
        engine.runAndWait()
        engine.stop()