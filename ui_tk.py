# ui_tk.py
import tkinter as tk
import threading
from tkinter import simpledialog
from timer import Timer

root = tk.Tk()
root.title("FocusT")
root.geometry("400x500")  # window to feel it


welcome_label = tk.Label(
    root, 
    text="Welcome to Focus T", 
    font=("Helvetica", 16, "bold"), 
    fg="red"
)

def start_timer():
    # Ask for minutes; Cancel returns None.
    minutes = simpledialog.askinteger("Start Timer", "Minutes:", minvalue=1)
    if minutes is None:
        return
    # timer in the background so the window stays responsive
    t = Timer()
    threading.Thread(target=t.start, args=(minutes,), daemon=True).start()
    


welcome_label.pack(pady=40)

root.mainloop()