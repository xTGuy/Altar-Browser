import tkinter as tk
from tkinter import ttk
from tkhtmlview import HTMLLabel

class TabbedBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Tabbed Browser")
        self.geometry("800x600")

        # Create Notebook (tabs)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Add initial tab
        self.add_tab()

        # Menu
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        tab_menu = tk.Menu(menubar, tearoff=0)
        tab_menu.add_command(label="New Tab", command=self.add_tab)
        tab_menu.add_command(label="Close Current Tab", command=self.close_tab)
        menubar.add_cascade(label="Tabs", menu=tab_menu)

    def add_tab(self):
        frame = ttk.Frame(self.notebook)

        # URL bar
        url_frame = ttk.Frame(frame)
        url_frame.pack(fill="x", pady=5, padx=5)

        url_entry = ttk.Entry(url_frame)
        url_entry.pack(side="left", fill="x", expand=True)

        go_button = ttk.Button(url_frame, text="Go", command=lambda: self.load_page(url_entry.get(), html_view))
        go_button.pack(side="left", padx=5)

        # HTML viewer
        html_view = HTMLLabel(frame, html="<h2>Welcome</h2><p>Type a local HTML or HTTP URL above.</p>")
        html_view.pack(fill="both", expand=True, padx=5, pady=5)

        self.notebook.add(frame, text="New Tab")
        self.notebook.select(frame)

    def load_page(self, url, html_view):
        try:
            if url.startswith("http"):
                import requests
                response = requests.get(url)
                html = response.text
            else:
                with open(url, 'r', encoding='utf-8') as file:
                    html = file.read()
            html_view.set_html(html)
        except Exception as e:
            html_view.set_html(f"<h2>Error</h2><p>{e}</p>")

    def close_tab(self):
        current = self.notebook.select()
        if current:
            self.notebook.forget(current)

if __name__ == "__main__":
    app = TabbedBrowser()
    app.mainloop()
