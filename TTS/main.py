from gtts import gTTS
import os

text = input('Enter Your Text: ')
language = 'en'

tts = gTTS(text=text, lang=language)
tts.save('tts.mp3')

os.system('start tts.mp3')