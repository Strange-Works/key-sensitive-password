import tkinter as tk
from pynput import keyboard
import threading

# Variables to track the state of Caps Lock and Shift
caps_lock_on = False
shift_pressed = False
password = []
key_details = []

def on_press(key):
    global caps_lock_on, shift_pressed, password, key_details

    try:
        # Check if Shift is pressed
        if key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            shift_pressed = True

        # Check if Caps Lock is toggled
        if key == keyboard.Key.caps_lock:
            caps_lock_on = not caps_lock_on

        # Detect alphanumeric keys and track their details
        if hasattr(key, 'char') and key.char:
            password.append(key.char)
            if key.char.isalpha():
                if caps_lock_on and not shift_pressed:
                    key_details.append((key.char, 'CapsLock'))
                elif shift_pressed and not caps_lock_on:
                    key_details.append((key.char, 'Shift'))
                elif caps_lock_on and shift_pressed:
                    key_details.append((key.char, 'CapsLock+Shift'))
                else:
                    key_details.append((key.char, 'Normal'))
            else:
                key_details.append((key.char, 'Normal'))

        # Update GUI with current password and key details
        update_gui()

    except AttributeError:
        pass

def on_release(key):
    global shift_pressed

    # Reset shift_pressed when Shift is released
    if key == keyboard.Key.shift or key == keyboard.Key.shift_r:
        shift_pressed = False

def update_gui():
    details_str = "\n".join([f"Key: {char}, Entered with: {detail}" for char, detail in key_details])
    details_label.config(text=f"Details of each key entered:\n{details_str}")

def start_key_listener():
    # Set up the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def on_password_entry(event):
    global password, key_details
    password = list(password_entry.get())
    key_details = []  # Clear previous details
    password_entry.delete(0, tk.END)  # Clear the password entry box

# Create the main window
root = tk.Tk()
root.title("Password Key Tracker")

# Set up the hacker-themed GUI
root.configure(bg='black')
root.geometry("600x400")

# Create and place labels
title_label = tk.Label(root, text="Enter your password:", font=("Courier", 16), fg="green", bg="black")
title_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Courier", 16), fg="green", bg="black", insertbackground='green')
password_entry.pack(pady=10)
password_entry.bind('<Return>', on_password_entry)

details_label = tk.Label(root, text="Details of each key entered:", font=("Courier", 12), fg="green", bg="black", wraplength=500, justify="left")
details_label.pack(pady=10)

# Start the key listener in a separate thread to avoid blocking the GUI
listener_thread = threading.Thread(target=start_key_listener, daemon=True)
listener_thread.start()

# Run the main loop
root.mainloop()
