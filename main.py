import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os

DATA_FILE = "students.csv"

class MarksAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marks Analyzer")
        self.root.geometry("600x400")

        self.setup_widgets()
        self.load_data()

    def setup_widgets(self):
        self.name_var = tk.StringVar()
        self.marks_var = tk.StringVar()

        tk.Label(self.root, text="Student Name").pack()
        self.name_entry = tk.Entry(self.root, textvariable=self.name_var)
        self.name_entry.pack()

        tk.Label(self.root, text="Marks (comma-separated)").pack()
        self.marks_entry = tk.Entry(self.root, textvariable=self.marks_var)
        self.marks_entry.pack()

        tk.Button(self.root, text="Add Record", command=self.add_record).pack(pady=5)
        tk.Button(self.root, text="Show All Records", command=self.show_records).pack()

        self.tree = ttk.Treeview(self.root, columns=("Name", "Total", "Average", "Grade"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill='both', expand=True)

    def grade_calc(self, avg):
        if avg >= 90: return 'A'
        elif avg >= 75: return 'B'
        elif avg >= 60: return 'C'
        elif avg >= 40: return 'D'
        else: return 'F'

    def add_record(self):
        name = self.name_var.get().strip()
        marks_str = self.marks_var.get().strip()

        if not name or not marks_str:
            messagebox.showwarning("Input Error", "Please enter both name and marks.")
            return

        try:
            marks = list(map(int, marks_str.split(',')))
            total = sum(marks)
            avg = total / len(marks)
            grade = self.grade_calc(avg)
        except:
            messagebox.showerror("Input Error", "Marks should be comma-separated integers.")
            return

        new_record = pd.DataFrame([[name, total, round(avg, 2), grade]],
                                  columns=["Name", "Total", "Average", "Grade"])

        if os.path.exists(DATA_FILE):
            df = pd.read_csv(DATA_FILE)
            df = pd.concat([df, new_record], ignore_index=True)
        else:
            df = new_record

        df.to_csv(DATA_FILE, index=False)
        messagebox.showinfo("Success", "Record added successfully.")
        self.name_var.set("")
        self.marks_var.set("")
        self.show_records()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            self.df = pd.read_csv(DATA_FILE)
        else:
            self.df = pd.DataFrame(columns=["Name", "Total", "Average", "Grade"])

    def show_records(self):
        self.load_data()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for _, row in self.df.iterrows():
            self.tree.insert("", "end", values=tuple(row))

if __name__ == "__main__":
    root = tk.Tk()
    app = MarksAnalyzerApp(root)
    root.mainloop()
