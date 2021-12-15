import tkinter
import math

check_mark = []
TIMER = None
reps = 1
press = 1

work = 25
short_break = 5
long_break = 15


def start_timer():
    work_sec = work * 60
    short_break_sec = short_break * 10
    long_break_sec = long_break * 15

    if reps % 8 == 0:
        title_label.config(text="LONG BREAK", fg="#FF1700")
        count_down(long_break_sec)
    elif reps % 2 == 0 and reps != 8:
        check_mark.append("✓")
        checkmark_label.config(text=check_mark)
        title_label.config(text="BREAK", fg="#FABB51")
        count_down(short_break_sec)
    else:
        title_label.config(text="WORK", fg="#7CD1B8")
        count_down(work_sec)


def count_down(total_sec):
    global reps, TIMER
    minute = math.floor(total_sec / 60)
    if minute < 10:
        minute = f"0{minute}"
    second = total_sec % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(canvas_label, text=f"{minute} : {second}")
    if total_sec > 0:
        TIMER = frame.after(1000, count_down, total_sec - 1)
    else:
        reps += 1
        start_timer()


def reset_timer():
    global reps
    canvas.after_cancel(TIMER)
    title_label.config(text="TIMER", fg="#A3423C")
    canvas.itemconfig(canvas_label, text="00 : 00")
    check_mark.clear()
    checkmark_label.config(text=check_mark)


frame = tkinter.Tk()
frame.title("POMODORO")
frame.config(padx=120, pady=50, bg="#04293A")
frame.minsize(width=600, height=400)

# button
reset_button = tkinter.Button(text="RESET", bd=0, width=10, font=("Arial", 18, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

start_button = tkinter.Button(text="START", bd=0, width=10, font=("Arial", 18, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

# canvas
canvas = tkinter.Canvas(width=200, height=224, bg="#04293A", highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_image)
canvas_label = canvas.create_text(100, 125, text="00 : 00", fill="white", font=("Arial", 35, "bold"))
canvas.grid(column=1, row=1)

# label
checkmark_label = tkinter.Label(text=check_mark, font=("Arial", 20, "bold"), fg="#519259", bg="#04293A")
checkmark_label.grid(column=1, row=3)

title_label = tkinter.Label(text="TIMER", font=("Arial", 50, "bold"), fg="#A3423C", bg="#04293A")
title_label.grid(column=1, row=0)


frame.mainloop()
