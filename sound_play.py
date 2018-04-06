from gtts import gTTS
import os
from playsound import playsound

def sound_play(soundtext):
    tts = gTTS(text='Alarm Alert. Alarm Alert.' + soundtext + soundtext, lang='en')
    tts.save("good.mp3")
    playsound("good.mp3")

# her voice *_*
