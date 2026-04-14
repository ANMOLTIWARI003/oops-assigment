import tkinter as tk
from tkinter import messagebox
import threading
import time
import winsound

running = False
paused = False
remaining_time = 0

# 🔊 Final loud sound
def final_sound():
    for _ in range(5):
        winsound.Beep(1200, 400)

# 🔊 Last 5 seconds beep
def countdown_beep():
    winsound.Beep(800, 200)

# Format time
def format_time(seconds):
    hrs, rem = divmod(seconds, 3600)
    mins, secs = divmod(rem, 60)
    return f"{hrs:02}:{mins:02}:{secs:02}"

# Countdown logic
def countdown():
    global remaining_time, running, paused

    while running and remaining_time > 0:
        if not paused:
            # 🔥 Play beep in last 5 seconds
            if remaining_time <= 5:
                countdown_beep()

            time.sleep(1)
            remaining_time -= 1
            timer_label.config(text=format_time(remaining_time))
        else:
            time.sleep(0.1)

    # 🔥 Final alarm
    if remaining_time == 0 and running:
        timer_label.config(text="00:00:00")
        final_sound()
        messagebox.showinfo("Done", "Time's up!")

    running = False

# Start
def start_timer():
    global running, remaining_time, paused

    if running:
        return

    try:
        hrs = int(hour_entry.get() or 0)
        mins = int(min_entry.get() or 0)
        secs = int(sec_entry.get() or 0)

        remaining_time = hrs*3600 + mins*60 + secs

        if remaining_time <= 0:
            messagebox.showwarning("Error", "Enter valid time")
            return

        running = True
        paused = False
        threading.Thread(target=countdown, daemon=True).start()

    except ValueError:
        messagebox.showerror("Error", "Only numbers allowed")

# Pause / Resume
def pause_timer():
    global paused
    paused = not paused

# Reset
def reset_timer():
    global running, remaining_time, paused
    running = False
    paused = False
    remaining_time = 0
    timer_label.config(text="00:00:00")

# GUI
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("350x420")
root.config(bg="#1e1e1e")

tk.Label(root, text="Countdown Timer", font=("Helvetica", 18, "bold"),
         bg="#1e1e1e", fg="white").pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

def create_entry(label_text):
    f = tk.Frame(frame, bg="#1e1e1e")
    f.pack(side="left", padx=10)
    tk.Label(f, text=label_text, fg="white", bg="#1e1e1e").pack()
    e = tk.Entry(f, width=5, font=("Helvetica", 14), justify="center")
    e.pack()
    return e

hour_entry = create_entry("HH")
min_entry = create_entry("MM")
sec_entry = create_entry("SS")

timer_label = tk.Label(root, text="00:00:00",
                       font=("Courier", 40, "bold"),
                       fg="#00ffcc", bg="#1e1e1e")
timer_label.pack(pady=30)

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack()

def create_btn(text, cmd, color):
    return tk.Button(btn_frame, text=text, command=cmd,
                     font=("Helvetica", 12, "bold"),
                     bg=color, fg="white", width=10, bd=0)

create_btn("Start", start_timer, "#28a745").grid(row=0, column=0, padx=5)
create_btn("Pause", pause_timer, "#ffc107").grid(row=0, column=1, padx=5)
create_btn("Reset", reset_timer, "#dc3545").grid(row=0, column=2, padx=5)

root.mainloop()