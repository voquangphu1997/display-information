import speech_recognition
import pyttsx3
from datetime import date

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
with speech_recognition.Microphone() as mic:
	print("Robot: I'm listening")
	audio = robot_ear.listen(mic)
print("Robot: ...")
try:
    you = robot_ear.recognize_google(audio)
except:
    you = "Please SPEAK"
print("Robot: " + you)
#hieu
you = "hello"
if you =="":
    robot_brain = "I can't hear you, try again"
elif you == "hello":
    robot_brain = "Hello Rita Vo"
elif you == "today":
    today = date.today()
    robot_brain = today.strftime("%B %d, %Y")
else:
    robot_brain = "I'm fine thank you and you"

print("Robot: " + robot_brain)
#noi



robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
