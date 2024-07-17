from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog


class MyWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF reader")
        self.frame = Frame(self)
        self.frame.pack()
        self.folderPath = StringVar()
        self.lblName = Label(self.frame, text="Open PDF file:")
        self.lblName.grid(row=0, column=0, sticky=W, pady=10, padx=(5, 0))
        self.entPath = Entry(self.frame, width=100, textvariable=self.folderPath)
        self.entPath.grid(row=0, column=1, sticky="we", pady=10, padx=10)
        self.btnFind = ttk.Button(self.frame, text="Browse Folder", command=self.set_folder_path)
        self.btnFind.grid(row=0, column=2, sticky=E, pady=10, padx=(0, 5))
        self.btnRead = Button(self.frame, text="Read PDF")
        self.btnRead.grid(row=1, column=1, pady=10, padx=10)


    @property
    def folder_path(self):
        return self.folderPath.get()

    def set_folder_path(self):
        folder_selected = filedialog.askopenfilename(filetypes=[("PDF", ".pdf")])
        self.folderPath.set(folder_selected)


    def empty_path(self):
        messagebox.showerror("Error", "Please select a PDF file")


    def wrong_pdf(self):
        messagebox.showerror("Could not read file", "The selected PDF file could not be read, please try with another file")