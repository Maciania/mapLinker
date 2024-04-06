import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import Tk, Text, BOTH, X, N, LEFT, RIGHT, END
from tkinter.ttk import Frame, Label, Entry, Button
import os
from tkinter import scrolledtext
import SinLib
from map import *
from omx import *
from PIL import Image,ImageTk




class MapLinker(Frame):

    def __init__(self):
        super().__init__()

        self.myMap = None  # Экземпляр класса для карты
        self.myOmx = None  # Экземпляр класса для OMX файла

        self.master.title("Map Linker XML")
        self.pack(fill=BOTH, expand=True)

        self.row1 = Frame(self)
        self.row1.pack(fill=X)

        self.header_r1 = Label(self.row1, text="Файл проекта OMX", width=18)
        self.header_r1.pack(side=LEFT, padx=2, pady=5)

        self.btn_open_omx = Button(self.row1, text='Открыть', command=self.select_omx_file)
        self.btn_open_omx.pack(side=RIGHT, padx=2, pady=5)

        self.entry_omx_path = Entry(self.row1)
        self.entry_omx_path.pack(fill=X, padx=2, expand=True)

        self.row2 = Frame(self)
        self.row2.pack(fill=X)

        self.header_r2 = Label(self.row2, text="Файл карты", width=18)
        self.header_r2.pack(side=LEFT, padx=2, pady=5)

        self.btn_open_map = Button(self.row2, text='Открыть', command=self.select_map_file)
        self.btn_open_map.pack(side=RIGHT, padx=2, pady=5)

        self.entry_map_path = Entry(self.row2)
        self.entry_map_path.pack(fill=X, padx=2, expand=True)

        self.st_omx_obj = scrolledtext.ScrolledText(self,
                                                    wrap=tk.WORD,
                                                    # width=40,
                                                    height=12,
                                                    font=("Times New Roman", 10)
                                                    )
        self.st_omx_obj.configure(state='disabled')
        self.st_omx_obj.pack(fill=X, padx=2, pady=2, expand=True)

        self.header_r3 = Label(self, text="", width=18)
        self.header_r3.pack(fill=X, padx=2, pady=2, expand=True)

        self.row4 = Frame(self)
        self.row4.pack(fill=X)

        self.header_r4 = Label(self.row4, text="node_path", width=18)
        self.header_r4.pack(side=LEFT, padx=2, pady=5)

        self.entry_node_path = Entry(self.row4)
        self.entry_node_path.pack(fill=X, padx=2, expand=True)
        self.entry_node_path.bind('<Return>', self.connect_node_path)
        self.entry_node_path['state'] = 'disabled'

        self.row5 = Frame(self)
        self.row5.pack(fill=X)

        self.header_r5 = Label(self.row5, text="node_id", width=18)
        self.header_r5.pack(side=LEFT, padx=2, pady=5)

        self.entry_node_id = Entry(self.row5)
        self.entry_node_id.pack(fill=X, padx=2, expand=True)
        self.entry_node_id.bind('<Return>', self.connect_node_id)
        self.entry_node_id['state'] = 'disabled'

        self.row6 = Frame(self)
        self.row6.pack(fill=X)

        self.btn_check_map = Button(self.row6, text='Проверить подвязку', command=self.check_linking_from_SinLib)
        self.btn_check_map.pack(side=RIGHT, padx=2, pady=5)

        self.btn_check_omx = Button(self.row6, text='Получить объекты', command=self.get_object_from_SinLib)
        self.btn_check_omx.pack(side=RIGHT, padx=2, pady=5)

        self.btn_link = Button(self.row6, text='Связать несвязанное', command=self.start_linking)
        self.btn_link.pack(side=RIGHT, padx=2, pady=5)


    # Выбор OMX файла
    def select_omx_file(self):
        filename = fd.askopenfilename(title='Open a file', initialdir=os.getcwd(), filetypes=[('All files', '*.omx')])
        self.entry_omx_path.delete(0, END)
        self.entry_omx_path.insert(0, filename)
        self.myOmx = OmxFile(omx_path=filename)

    # Получаем список объектов в директории SinLib
    def get_object_from_SinLib(self):
        if isinstance(self.myOmx, OmxFile):
            self.clear_st()
            self.insert_to_st("Путь поиска: AstraRegul => IOS_App => SinLib\n")
            cnt = 0
            for i in self.myOmx.get_SinLib_struct():
                cnt += 1
                self.insert_to_st(f'{cnt}.Имя: {i:<10} Тип: {self.myOmx.get_Obj_base_type(i)}')

    # Вставка в ST
    def insert_to_st(self, text):
        self.st_omx_obj.configure(state='normal')
        self.st_omx_obj.insert(tk.INSERT, text + '\n')
        self.st_omx_obj.configure(state='disabled')

    # Очистить scrolled text
    def clear_st(self):
        self.st_omx_obj.configure(state='normal')
        self.st_omx_obj.delete('1.0', END)
        self.st_omx_obj.configure(state='disabled')

    # Вставка в node_path
    def insert_to_node_path(self, text):
        self.entry_node_path.configure(state='normal')
        self.entry_node_path.delete(0, END)
        self.entry_node_path.insert(tk.INSERT, text)
        self.entry_node_path.configure(state='disabled')

    # Вставка в node_id
    def insert_to_node_id(self, text):
        self.entry_node_id.configure(state='normal')
        self.entry_node_id.delete(0, END)
        self.entry_node_id.insert(tk.INSERT, text)
        self.entry_node_id.configure(state='disabled')

    # Выбор файла с картой
    def select_map_file(self):
        filename = fd.askopenfilename(title='Open a file', initialdir=os.getcwd(), filetypes=[('All files', '*.xml')])
        self.entry_map_path.delete(0, END)
        self.entry_map_path.insert(0, filename)

        self.myMap = MapFile(map_path=filename)

    # Получаем список объектов в директории SinLib
    def check_linking_from_SinLib(self):
        if isinstance(self.myMap, MapFile) and isinstance(self.myOmx, OmxFile):
            self.clear_st()
            self.insert_to_st("Путь поиска: AstraRegul => IOS_App => SinLib, подвязки\n")
            cnt = 0
            for i in self.myOmx.get_SinLib_struct():
                cnt += 1
                self.insert_to_st(
                    f'{cnt}.Имя: {i:<10} Тип: {self.myOmx.get_Obj_base_type(i)}'
                    f'{"Статус подвязки:":>20}{self.myMap.check_linking(i)}'
                )

    # сохранить тег в файл
    def save_map(self):
        self.myMap.write_XML_to_map()

    # Установить значение переменной node_path_tag при нажатии Enter в поле ввода entry_node_path
    def connect_node_path(self, event):
        node_path_tag.set(self.entry_node_path.get())
        self.entry_node_path.delete(0, END)

    # Установить значение переменной node_path_tag при нажатии Enter в поле ввода entry_node_path
    def connect_node_id(self, event):
        node_id_tag.set(self.entry_node_id.get())
        self.entry_node_id.delete(0, END)

    # Связвание объектов
    def start_linking(self):

        global linkink_object
        self.btn_link['text'] = 'Связывание'
        self.clear_st()
        # Для каждого объекта в IOs_App проверить подвязку
        for i in self.myOmx.get_SinLib_struct():
            if not self.myMap.check_linking(i):
                # Проверяем на принадлежность библиотеке
                if self.myOmx.get_Obj_library_type(i) == 'SineticLib':

                    # Проверка на принадлежность типу DI библиотеке SineticLib
                    if self.myOmx.get_Obj_base_type(i) == 'DI1':
                        linkink_object = SinLib.DI(self.get_node_path(i), self.get_node_id(i))

                    # AI
                    if self.myOmx.get_Obj_base_type(i) == 'AI1':
                        linkink_object = SinLib.AI(self.get_node_path(i), self.get_node_id(i))

                    # VLVD
                    if self.myOmx.get_Obj_base_type(i) == 'VLV_D':
                        linkink_object = SinLib.VLVD(self.get_node_path(i), self.get_node_id(i))

                    # VLVA
                    if self.myOmx.get_Obj_base_type(i) == 'VLV_A':
                        linkink_object = SinLib.VLVA(self.get_node_path(i), self.get_node_id(i))

                    # MTR
                    if self.myOmx.get_Obj_base_type(i) == 'MTR':
                        linkink_object = SinLib.MTR(self.get_node_path(i), self.get_node_id(i))

                    # PID
                    if self.myOmx.get_Obj_base_type(i) == 'PID_A':
                        linkink_object = SinLib.PID(self.get_node_path(i), self.get_node_id(i))

                    for j in range(linkink_object.loopCnt()):
                        xmlObj = self.myMap.create_XMLtag(linkink_object[j][0], linkink_object[j][1])  # создаем объект тега
                        self.myMap.insert_XML_to_map(xmlObj)  # вставляем объект в карту


        self.btn_link['text'] = 'Связать несвязанное'
        self.header_r3['text'] = ''
        self.save_map()  # сохраняем файл
        self.insert_to_st('Карта подвязки успешно обновлена')

    # Получить node-path объекта по имени и произвести процедуры с полем ввода
    def get_node_path(self, object_name):

        # Ждем ввода в поле node_path, подставляем туда node_path из свойства объекта
        self.header_r3[
            'text'] = f'Связать {object_name} Тип: {self.myOmx.get_Obj_base_type(object_name)}, подтверди node_path <ENTER>'
        self.insert_to_node_path(self.myOmx.get_Obj_node_path(object_name))  # Вставляем в поле путь до объекта
        self.entry_node_path.configure(state='normal')  # активируем поле для ввода
        self.entry_node_path.focus_set()  # устанавливаем курсор в поле
        root.wait_variable(node_path_tag)  # ждем ввода значения и нажатия Enter в поле
        node_path = node_path_tag.get()  # Получаем значения поля после нажатия кнопки Enter
        self.entry_node_path.configure(state='disabled')  # деактивируем поле
        self.insert_to_st(
            f'Типу: {self.myOmx.get_Obj_base_type(object_name)} присвоен node_path: {node_path}')  # логируем

        return node_path

    # Аналогично получаем node_id
    def get_node_id(self, object_name):
        self.header_r3[
            'text'] = f'Связать {object_name} Тип: {self.myOmx.get_Obj_base_type(object_name)}, подтверди node_id <ENTER>'
        self.insert_to_node_id(self.myOmx.get_Obj_node_id(object_name))
        self.entry_node_id.configure(state='normal')
        self.entry_node_id.focus_set()  # устанавливаем курсор в поле
        root.wait_variable(node_id_tag)  # ждем ввода значения и нажатия Enter в поле
        node_id = node_id_tag.get()
        self.entry_node_id.configure(state='disabled')
        self.insert_to_st(f'Типу: {self.myOmx.get_Obj_base_type(object_name)} присвоен node_id: {node_id}')

        return node_id


    def test_func(self):
        print(self.myOmx.get_Obj_library_type('di'))


if __name__ == '__main__':
    root = Tk()
    node_path_tag = tk.StringVar()  # тег ПЛК
    node_id_tag = tk.StringVar()  # тег ПЛК
    root.geometry("500x380")
    app = MapLinker()
    root.mainloop()

