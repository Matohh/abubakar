import tkinter as tk

class DictionaryApp:
    def __init__(self, master):
        self.master = master
        self.dict = {}
        self.create_widgets()

    def create_widgets(self):
        self.key_entry = tk.Entry(self.master)
        self.key_entry.pack()

        self.value_entry = tk.Entry(self.master)
        self.value_entry.pack()

        self.add_button = tk.Button(self.master, text="Add", command=self.add_to_dict)
        self.add_button.pack()

        self.show_button = tk.Button(self.master, text="Show", command=self.show_dict)
        self.show_button.pack()

    def add_to_dict(self):
        key = self.key_entry.get()
        value = self.value_entry.get()
        self.dict[key] = value

    def show_dict(self):
        result = ""
        for key, value in self.dict.items():
            result += f"{key}: {value}\n"
        tk.messagebox.showinfo("Dictionary", result)

root = tk.Tk()
app = DictionaryApp(root)
root.mainloop()






