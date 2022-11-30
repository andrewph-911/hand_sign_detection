import pyttsx3
from pyttsx3 import Engine

# text = ["What's your name?", "Hello", "Nice to meet you", "I am so sorry"]
labels = ["BACK", "CLOSE", "DISLIKE", "GOOD", "HELLO", "I Love you", "OKAY", "OPEN", "SORRY", "STOP", "THANKS"]
engine: Engine = pyttsx3.init()
engine.say(labels)
engine.runAndWait()
print(labels)
