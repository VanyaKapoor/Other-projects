import tkinter  as t
import pyttsx3
engine = pyttsx3.init()
clock = t.Tk()
clock.state("zoomed")
clock.title("Text to speech")

def talk():
    string = str(user_input.get())
    engine.say(string)
    engine.runAndWait()


label = t.Label(clock, text = "Write your msg below", font = ("arial", 32, "bold"),bg = "yellow", fg = "blue" )
label.pack(pady = 20)

user_input = t.Entry(clock, font = ("Times New Roman", 32, "bold"),bg = "blue", fg = "black", width = 20)
user_input.pack(pady = 20)

button = t.Button(clock, text = "SPEECH!", font = ("Times New Roman", 32, "bold"),bg = "white", fg = "black", width = 20, command = talk)
button.pack(pady = 20)
clock.mainloop()




