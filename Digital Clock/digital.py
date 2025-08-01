import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("🕒 Advanced Digital Clock")
        self.root.geometry("520x400")
        self.root.resizable(False, False)

        self.is_dark = False
        self.is_24_hour = True
        self.timezone = time.tzname[0]  # System timezone

        self.create_widgets()
        self.apply_theme()
        self.update_clock()

    def create_widgets(self):
        self.style = ttk.Style(self.root)

        # Main container
        self.container = tk.Frame(self.root, bd=5, relief="ridge")
        self.container.pack(pady=20, padx=20, fill="both", expand=True)

        self.title_label = tk.Label(self.container, text="🕒 Digital Clock", font=("Arial", 26, "bold"))
        self.title_label.pack(pady=(15, 5))

        self.time_label = tk.Label(self.container, text="", font=("Courier New", 48, "bold"))
        self.time_label.pack(pady=(10, 5))

        self.date_label = tk.Label(self.container, text="", font=("Arial", 14))
        self.date_label.pack(pady=(0, 5))

        self.timezone_label = tk.Label(self.container, text="", font=("Arial", 12, "italic"))
        self.timezone_label.pack()

        # Button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.theme_btn = ttk.Button(self.button_frame, text="🌗 Toggle Theme", command=self.toggle_theme)
        self.theme_btn.grid(row=0, column=0, padx=10)

        self.format_btn = ttk.Button(self.button_frame, text="🕐 Switch Format", command=self.toggle_time_format)
        self.format_btn.grid(row=0, column=1, padx=10)

        # Tooltips
        self.tooltip = tk.Label(self.root, text="", bg="#ffffe0", fg="#333", font=("Arial", 9), bd=1, relief="solid")
        self.tooltip.place_forget()

        self.theme_btn.bind("<Enter>", lambda e: self.show_tooltip("Switch between Light/Dark mode"))
        self.format_btn.bind("<Enter>", lambda e: self.show_tooltip("Toggle 12H/24H format"))
        self.theme_btn.bind("<Leave>", self.hide_tooltip)
        self.format_btn.bind("<Leave>", self.hide_tooltip)

    def update_clock(self):
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S") if self.is_24_hour else now.strftime("%I:%M:%S %p")
        date_str = now.strftime("%A, %d %B %Y")

        self.time_label.config(text=time_str)
        self.date_label.config(text=date_str)
        self.timezone_label.config(text=f"Time Zone: {self.timezone}")
        self.root.after(1000, self.update_clock)

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.apply_theme()

    def toggle_time_format(self):
        self.is_24_hour = not self.is_24_hour

    def apply_theme(self):
        if self.is_dark:
            bg = "#1e1e1e"
            fg = "#ffffff"
            highlight = "#00ffcc"
            container_bg = "#2b2b2b"
        else:
            bg = "#e6f2ff"
            fg = "#000000"
            highlight = "#000080"
            container_bg = "#ffffff"

        self.root.configure(bg=bg)
        self.container.configure(bg=container_bg)

        for widget in [self.title_label, self.time_label, self.date_label, self.timezone_label]:
            widget.configure(bg=container_bg, fg=highlight if widget == self.time_label else fg)

    def show_tooltip(self, text):
        self.tooltip.config(text=text)
        self.tooltip.place(relx=0.5, rely=1.02, anchor="n")

    def hide_tooltip(self, event):
        self.tooltip.place_forget()


# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
