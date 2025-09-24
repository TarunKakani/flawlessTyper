import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time

pyautogui.FAILSAFE = True

def type_code_flawlessly(text):
    """
    The most robust typing method. It uses a single, unified loop 
    to handle all lines consistently, preventing timing and indentation errors.
    """
    try:
        lines = text.splitlines()
        
        for i, line in enumerate(lines):
            # Type the line's content, stripped of its original indent.
            # This lets the editor's auto-indent do all the work.
            pyautogui.typewrite(line.lstrip())

            # Press Enter after every line EXCEPT the very last one.
            if i < len(lines) - 1:
                pyautogui.press('enter')
                # A brief pause is crucial for the editor to catch up.
                # Increase this if your online editor is slow.
                time.sleep(0.05) 
            
        print("Flawless typing complete!")
    except Exception as e:
        print(f"An error occurred during typing: {e}")


def start_typing_thread():
    """Starts the typing function in a new thread after a delay."""
    text = input_text.get("1.0", "end-1c")
    if text:
        print("Typing in 5 seconds... Click on the target text field now.")
        root.after(5000, lambda: threading.Thread(target=type_code_flawlessly, args=(text,)).start())

# --- GUI Setup ---
root = tk.Tk()
root.title("Flawless Typer")
root.geometry("400x300")
root.configure(bg="#4B0082")

style = ttk.Style()
style.theme_use('clam')
style.configure('.', background='#4B0082', foreground='white')
style.configure('TButton', background='#6a0dad', foreground='white', borderwidth=1)
style.map('TButton', background=[('active', '#8a2be2')])
style.configure('TLabel', background='#4B0082', foreground='white', font=('Helvetica', 10))

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

input_label = ttk.Label(main_frame, text="Enter code to type:")
input_label.pack(pady=(0, 5))

input_text = tk.Text(main_frame, width=40, height=10, bg="#2e0854", fg="white", insertbackground="white", relief="sunken", borderwidth=2)
input_text.pack(pady=5)

type_button = ttk.Button(main_frame, text="Type Code (after 5s)", command=start_typing_thread)
type_button.pack(pady=5)

root.mainloop()