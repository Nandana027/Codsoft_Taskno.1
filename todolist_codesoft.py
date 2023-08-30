import tkinter as tk

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do-List")
        self.items = []

        self.label = tk.Label(root, text="Enter the Tasks")  # Added 'text=' to specify the label text
        self.label.pack()

        self.entry = tk.Entry(root, width=30, borderwidth=5)
        self.entry.pack()

        self.ta_button = tk.Button(root, text="Add Tasks", command=self.add_tasks)  # Fixed command parameter
        self.ta_button.pack()

        self.lb = tk.Listbox(root)
        self.lb.pack()

        self.tr_button = tk.Button(root, text="Remove Task", command=self.remove_tasks)  # Fixed command parameter
        self.tr_button.pack()  # Added '()' to call the pack method

    def add_tasks(self):
        task = self.entry.get()
        if task:
            self.items.append(task)
            self.update_list()

    def remove_tasks(self):
        sel_task = self.lb.curselection()
        if sel_task:
            index = sel_task[0]
            del self.items[index]
            self.update_list()

    def update_list(self):
        self.lb.delete(0, tk.END)
        for task in self.items:
            self.lb.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    tdl = ToDoList(root)
    root.mainloop()
