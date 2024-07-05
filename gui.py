import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import Tk, Text, BOTH, X, N, LEFT, RIGHT, END
from tkinter.ttk import Frame, Label, Entry, Button
from tkinter import scrolledtext


class MyFileDialog(Frame):
    """Класс с контейнером из трех элементов для выбора файла из директории проекта
    Используется для выбора файла проекта *omx и файла карты в который добавляются привязки"""

    def __init__(self, labelTxt: str, btnTxt: str, cmd, master=None):
        super().__init__(master)
        self.__init(labelTxt, btnTxt, cmd)

    def __init(self, labelTxt, btnTxt, cmd):
        self.label = Label(self, text=labelTxt)
        self.entry = Entry(self, state='disabled')
        self.btn = Button(self, text=btnTxt, command=cmd)
        self.__packing()

    def __packing(self):
        self.label.pack(side="left", padx=10)
        self.entry.pack(side="left", expand=True, fill=X)
        self.btn.pack(side="left", padx=10)

    def setNewTxt(self, newText):
        self.entry.configure(state='normal')
        self.entry.delete(0, END)
        self.entry.insert(tk.INSERT, newText)
        self.entry.configure(state='disabled')

    def getText(self):
        return self.entry.get()


class MyComboBox(Frame):
    """Класс с контейнером из двух элементов для выбора поля из комбобокса
    Используется для выбора объектов внутри проекта"""

    def __init__(self, labelTxt, bindCombo, master=None):
        super().__init__(master)
        self.__init(labelTxt, bindCombo)

    def __init(self, labelTxt, bindCombo):
        self.label = Label(self, text=labelTxt)
        self.combo = ttk.Combobox(self)
        if bindCombo is not None:
            self.combo.bind("<<ComboboxSelected>>", bindCombo)
        self.__packing()

    def __packing(self):
        self.label.pack(side="left", padx=10)
        self.combo.pack(side="left", expand=True, fill=X)

    def setValues(self, values):
        self.combo['values'] = values
        self.combo.current(0)

    def getValue(self):
        return self.combo.get()


class MyLabelFrame(Frame):
    """Класс с контейнером из двух элементов для вывода объектов участвующих в подвязке
    Используется для вывода node_path и node_id"""

    def __init__(self, labelTxt, bindEntry, master=None):
        super().__init__(master)
        self.__init(labelTxt, bindEntry)

    def __init(self, labelTxt, bindEntry):
        self.label = Label(self, text=labelTxt)
        self.entry = Entry(self, state='disabled')
        if bindEntry is not None:
            self.entry.bind("<Return>", bindEntry)
        self.__packing()

    def __packing(self):
        self.label.pack(side="left", padx=10)
        self.entry.pack(side="left", expand=True, fill=X)

    def setNewTxt(self, newText):
        self.enable()
        self.entry.delete(0, END)
        self.entry.insert(tk.INSERT, newText)
        self.disable()

    def enable(self):
        self.entry.configure(state='normal')

    def disable(self):
        self.entry.configure(state='disabled')

    def setFocus(self):
        self.entry.focus_set()

    def getValue(self):
        return self.entry.get()

    def clear(self):
        self.enable()
        self.entry.delete(0, END)
        self.disable()


class ControlField(Frame):
    """Класс с контейнером из неограниченного кол-ва кнопок
    Используется для управления процессом подвязки
    В качестве входный аргументов используются кортежи из двух элементов - название кнопки и ее команда """

    def __init__(self, *args, master=None):
        super().__init__(master)
        self.__init(*args)

    def __init(self, *args):
        self.btnLst = [Button(self, text=btn[0], command=btn[1]) for btn in args]
        self.__packing()

    def __packing(self):
        for btn in self.btnLst:
            btn.pack(side="left", padx=2, expand=True, fill=X)


class MyScrollText(Frame):
    """Класс прокручиваемого текста """

    def __init__(self, master=None):
        super().__init__(master)
        self.__init()

    def __init(self):
        self.sTxt = scrolledtext.ScrolledText(self,
                                              wrap=tk.WORD,
                                              height=4,
                                              font=("Times New Roman", 10),
                                              state='disabled'
                                              )

        self.__packing()

    def __packing(self):
        self.sTxt.pack(side="left", padx=10, expand=True, fill=X)

    def setNewTxt(self, newText):
        self.sTxt.configure(state='normal')
        # self.sTxt.delete('1.0', END)
        self.sTxt.insert(tk.INSERT, newText + '\n')
        self.sTxt.configure(state='disabled')

    def clear(self):
        self.sTxt.configure(state='normal')
        self.sTxt.delete('1.0', END)
        self.sTxt.configure(state='disabled')


class MyTable(Frame):
    """Таблица для представления объектов с указанием нозвания объекта, его базового типа и статусом подвязки"""

    def __init__(self, master=None):
        super().__init__(master)
        self.__init()

    def __init(self):
        columns = ("#1", "#2", "#3", "#4", "#5")
        self.tree = ttk.Treeview(self, show="headings", columns=columns)
        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Название")
        self.tree.heading("#3", text="Тип")
        self.tree.heading("#4", text="Библиотека")
        self.tree.heading("#5", text="Статус подвязки")

        self.tree.column("#1", width=10)
        self.tree.column("#2", width=20)
        self.tree.column("#3", width=20)
        self.tree.column("#4", width=30)
        self.tree.column("#5", width=70)

        self.ysb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.ysb.set)
        self.__packing()

    def __packing(self):
        self.tree.pack(side="left", padx=10, expand=True, fill=X)
        self.ysb.pack(side="left",  fill=BOTH)

    def insert(self, obj_id, obj_name: str, obj_type: str, base_type: str, con_status: str):
        self.tree.insert("", END, values=(obj_id, obj_name, obj_type, base_type, con_status))

    def clear(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
