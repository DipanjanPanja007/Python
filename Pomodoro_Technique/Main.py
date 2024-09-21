import math
from tkinter import *

PINK = "#e2979c"
RED = "#dc143c"
GREEN = "#32cd32"
YELLOW = "#ffffd6"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
cycle = 0
work_count = 0


def reset():
    global timer
    global cycle
    global work_count
    window.after_cancel(timer)
    title_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    cycle = 0
    work_count = 0


def start_timer():
    global cycle
    cycle += 1
    global work_count

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # time for long break
    if cycle % 8 == 0 :
        title_label.config(text="Well Done, have some rest", fg=PINK)
        count_down(long_break_sec)

    # time for short break
    elif cycle % 2 == 0:
        title_label.config(text="Take a break", fg=RED)
        count_down(short_break_sec)

    # time for work
    else:
        title_label.config(text="Work Time", fg=GREEN)
        count_down(work_sec)
        # check_marks.config(text=f"{check_marks.cget('text')}✔️")
        work_count += 1
        work_progress = ""
        for tick in range(work_count - 1):
            work_progress += " ✔ "
        check_marks.config(text=work_progress)


def count_down(count):
    count_min = math.floor(count/60)
    count_sec =  count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()


window = Tk()
window.title("Pomodoro")
window.config(padx=30,pady=50,bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME,44))
title_label.grid(column=1, row= 0)

canvas = Canvas(width=440, height=430, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(220,215,image=tomato_img)

timer_text = canvas.create_text(220,280, text=f"00:00", fill="white", font=(FONT_NAME,44))
canvas.grid(column=1, row=1)
# count_down(5)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)
reset_button = Button(text="Reset", highlightthickness=0,command=reset)
reset_button.grid(column=2,row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(20))
check_marks.grid(column=1, row=3)

window.mainloop()



