import tkinter as tk

#VAR
count = -1 #initially
run = False # not running

def var(stopwatch_label):
    def value():
        if run: # click on start
            global count
            if count == -1:
                show = "STARTING STOPWATCH..."
            else:
                show = str(count)
            stopwatch_label["text"] = show #setting text for label using show var
            stopwatch_label.after(1000,value) # 1000mi == 1sec
            count  +=1
    value()

def start(stopwatch_label):
    global run
    run = True
    var(stopwatch_label)
    btn1["state"] = "disabled"
    btn2["state"] = "normal"
    btn3["state"] = "normal"

def stop():
    global run
    run = False
    btn1["state"] = "normal"
    btn2["state"] = "disabled"
    btn3["state"] = "normal"

def reset(stopwatch_label):
    global count
    count= -1 #initial
    if run == False :
        btn3["state"] = "disabled"
        stopwatch_label["text"] = "WELCOME"
    else:
        stopwatch_label["text"] = "START"

# creating window
window = tk.Tk()
#set size
window.minsize(width = 400, height = 200)

#Window background
window.configure(background = "turquoise")

#set title
window.title("COOL STOPWATCH")

#CREATE LABEL
stopwatch_label = tk.Label(window, text = "WELCOME", fg = "blue", font = "Times 25 bold", bg = "yellow") #fg = for ground

stopwatch_label.pack() #shows the label # imp

#BUTTONS
btn1 = tk.Button(window, text = "START", fg = "pink", font = "Times 15 underline", bg = "purple", width = 15, height = 2, command = lambda:start(stopwatch_label)) #lambda because of arg
btn1.pack()
btn2 = tk.Button(window, text = "STOP", fg = "pink", font = "Times 15 underline", bg = "purple", width = 15, height = 2, state = "disabled", command = stop)
btn2.pack()
btn3 = tk.Button(window, text = "RESET", fg = "pink", font = "Times 15 underline", bg = "purple", width = 15, height = 2, state = "disabled", command = lambda:reset(stopwatch_label))
btn3.pack()


window.mainloop() # at end
