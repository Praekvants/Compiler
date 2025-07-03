import os, pandas as pd, tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog

def merge(paths):
    df   = pd.concat((pd.read_csv(p) for p in paths), ignore_index=True)
    base = os.path.splitext(os.path.basename(paths[0]))[0]       # full name of first file
    desk = os.path.join(os.path.expanduser("~"), "Desktop")
    out_dir  = os.path.join(desk, f"Merged_{base}")              # folder
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, f"Merged_{base}.csv")       # file
    df.to_csv(out_file, index=False)
    print("✓ saved", out_file)

class Compiler(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Compiler")
        self.geometry("600x300")
        drop = tk.Label(self, text="Drag CSV files here")
        drop.pack(expand=True, fill="both")
        drop.drop_target_register(DND_FILES)
        drop.dnd_bind("<<Drop>>", lambda e: merge(self.tk.splitlist(e.data)))
        tk.Button(self, text="Browse", command=self._browse).pack(pady=6)

    def _browse(self):
        files = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])
        if files: merge(files)

if __name__ == "__main__":
    Compiler().mainloop()
