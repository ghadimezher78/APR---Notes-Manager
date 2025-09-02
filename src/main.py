import tkinter as tk
from tkinter import simpledialog, messagebox

class APRApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("APR - Notes Manager")
        self.geometry("400x400")
        self.notes = []
        self.resizable(False,False)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X)

        tk.Button(btn_frame, text="Add Note", command=self.add_note).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text="Delete Note", command=self.delete_note).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text="Edit Note", command=self.edit_note).pack(side=tk.LEFT, padx=5, pady=5)

    def add_note(self):
        note = simpledialog.askstring("Add Note", "Enter your note:")
        if note:
            self.notes.append(note)
            self.listbox.insert(tk.END, note)

    def delete_note(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.listbox.delete(idx)
            del self.notes[idx]
        else:
            messagebox.showinfo("Delete Note", "No note selected.")

    def edit_note(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            current_note = self.notes[idx]
            new_note = simpledialog.askstring("Edit The Note", "Edit The Note:", initialvalue=current_note)
            if new_note:
                self.notes[idx] = new_note
                self.listbox.delete(idx)
                self.listbox.insert(idx, new_note)
            else:
                messagebox.showinfo("Edit Note", "a Note Is Not Selected")    
            


if __name__ == "__main__":
    app = APRApp()
    app.mainloop()