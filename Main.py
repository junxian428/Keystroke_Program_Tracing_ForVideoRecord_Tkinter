import tkinter as tk
import keyboard
import time

WINDOW_WIDTH = 200
WINDOW_HEIGHT = 50
MAX_WINDOWS = 5
FADE_TIMEOUT = 2000
FADE_INTERVAL = 10
FADE_STEP = 0.1
BACKGROUND_COLOR = "#808080"
TRANSPARENCY = 0.8

class KeystrokeWindow:
    def __init__(self, keystroke):
        self.window = tk.Toplevel(root)
        self.window.overrideredirect(True)
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+10+{root.winfo_screenheight() - WINDOW_HEIGHT - 10}")
        self.window.configure(bg=BACKGROUND_COLOR)
        self.window.attributes("-topmost", True)
        self.window.attributes("-alpha", TRANSPARENCY)
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)

        self.label = tk.Label(self.window, text=keystroke, font=("Courier New", 24), fg="white", bg=BACKGROUND_COLOR)
        self.label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.fade_after_id = self.window.after(FADE_TIMEOUT, self.fade_out)

    def close_window(self):
        if self.window is not None:
            self.window.destroy()
            self.window = None

    def fade_out(self):
        if self.window is None:
            return

        alpha = TRANSPARENCY
        while alpha > 0:
            alpha -= FADE_STEP
            if self.window is not None:
                self.window.attributes("-alpha", alpha)
                self.window.update()
                time.sleep(FADE_INTERVAL / 1000)

        self.close_window()


def on_key_press(event):
    keystroke = event.name
    if not keystroke_windows:
        fade_all_windows()
    keystroke_windows.append(KeystrokeWindow(keystroke))
    if len(keystroke_windows) > MAX_WINDOWS:
        oldest_window = keystroke_windows.pop(0)
        oldest_window.close_window()
    move_windows_up()


def fade_all_windows():
    for window in keystroke_windows:
        window.fade_out()


def move_windows_up():
    for i, window in enumerate(keystroke_windows):
        if window.window is not None:
            y_position = root.winfo_screenheight() - (len(keystroke_windows) - i) * (WINDOW_HEIGHT + 10)
            window.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+10+{y_position}")


def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Keystroke Capture")
root.configure(bg=BACKGROUND_COLOR)
root.wm_attributes("-transparentcolor", BACKGROUND_COLOR)

keystroke_windows = []

keyboard.on_press(on_key_press)

exit_button = tk.Button(root, text="Exit", command=exit_app, bg=BACKGROUND_COLOR, fg="white")
exit_button.pack(pady=10)

root.mainloop()
