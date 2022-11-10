from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, checks
    reps = 0
    checks = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    work = WORK_MIN * 60
    if reps % 8 == 0:
        display_countdown(long_break)
        title.config(text="Long break", fg=GREEN)

    elif reps % 2 == 0:
        display_countdown(short_break)
        title.config(text="Short break", fg=PINK)

    else:
        display_countdown(work)
        title.config(text="Work", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def display_countdown(count):
    global checks, timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        timer = window.after(1000, display_countdown, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks += 1
            check_mark.config(text="✔"*checks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Tytul
title = Label(text="Timer", font=(FONT_NAME, 28, "normal"), fg=GREEN, highlightthickness=0, bg=YELLOW)
title.grid(row=0, column=1, pady=(0, 25), padx=(15, 0))

# Pomidor
photo = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=1)

# Przyciski
start = Button(text="start", bg=GREEN, command=start_timer)
start.grid(row=2, column=0, pady=(20, 0))

reset = Button(text="reset", bg=GREEN, command=reset_timer)
reset.grid(row=2, column=2, pady=(20, 0))

# Ptaszki
check_mark = Label(fg="GREEN", bg=YELLOW, font=(FONT_NAME, 14, "normal"))
check_mark.grid(row=3, column=1)

window.mainloop()
