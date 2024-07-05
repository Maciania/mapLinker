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
from gui import *


class MapLinker(Frame):

    def __init__(self):
        super().__init__()

        self.myMap = None  # Экземпляр класса для карты
        self.myOmx = None  # Экземпляр класса для OMX файла
        self.master.title("Map Linker XML")

        # Заменяем все что ниже на объекты
        self.fields = {
            'omx': MyFileDialog('Файл проекта OMX :', 'Открыть', cmd=self.select_omx_file),
            'map': MyFileDialog('Файл карты :', 'Открыть', cmd=self.select_map_file),
            'iosObj': MyComboBox('Список объектов в IosApp :', bindCombo=self.selected_iosApp),
            'iosType': MyComboBox('Тип :', bindCombo=None),
            'table': MyTable(),
            'log': MyScrollText(),
            'nodePath': MyLabelFrame('NodePath :', bindEntry=self.connect_node_path),
            'nodeId': MyLabelFrame('NodeId :', bindEntry=self.connect_node_id),
            'btn': ControlField(
                ('Проверить подвязку', self.checkLinking),
                ('Получить объекты', self.get_obj),
                ('Связать несвязанное', self.start_linking)
            )
        }

        self.__packing()
        """
        # Строка №1
        self.row1 = Frame(self)
        self.row1.pack(fill=X)

        self.header_r1 = Label(self.row1, text="Файл проекта OMX", width=18)
        self.header_r1.pack(side=LEFT, padx=2, pady=5)

        self.btn_open_omx = Button(self.row1, text='Открыть', command=self.select_omx_file)
        self.btn_open_omx.pack(side=RIGHT, padx=2, pady=5)

        self.entry_omx_path = Entry(self.row1)
        self.entry_omx_path.pack(fill=X, padx=2, expand=True)

        # Строка №2
        self.row2 = Frame(self)
        self.row2.pack(fill=X)

        self.header_r2 = Label(self.row2, text="Файл карты", width=18)
        self.header_r2.pack(side=LEFT, padx=2, pady=5)

        self.btn_open_map = Button(self.row2, text='Открыть', command=self.select_map_file)
        self.btn_open_map.pack(side=RIGHT, padx=2, pady=5)

        self.entry_map_path = Entry(self.row2)
        self.entry_map_path.pack(fill=X, padx=2, expand=True)

        # Строка №3
        self.row3 = Frame(self)
        self.row3.pack(fill=X)

        self.header_r3 = Label(self.row3, text="Список объектов в IosApp", width=24)
        self.header_r3.pack(side=LEFT, padx=2, pady=5)

        self.cbIosApp = ttk.Combobox(self.row3, values=self.iosAppObj, width=20)
        self.cbIosApp.bind("<<ComboboxSelected>>", self.selected_iosApp)
        self.cbIosApp.pack(side=LEFT, padx=2, pady=5)

        self.cbTypes = ttk.Combobox(self.row3, width=20)
        self.cbTypes.pack(side=RIGHT, padx=2, pady=5)

        self.header_types_r3 = Label(self.row3, text="Тип")
        self.header_types_r3.pack(side=RIGHT, padx=2, pady=5)

        # Читай между строк. Текстовое поля для логов
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

        # Строка №4
        self.row4 = Frame(self)
        self.row4.pack(fill=X)

        self.header_r4 = Label(self.row4, text="node_path", width=18)
        self.header_r4.pack(side=LEFT, padx=2, pady=5)

        self.entry_node_path = Entry(self.row4)
        self.entry_node_path.pack(fill=X, padx=2, expand=True)
        self.entry_node_path.bind('<Return>', self.connect_node_path)
        self.entry_node_path['state'] = 'disabled'

        # Строка №5
        self.row5 = Frame(self)
        self.row5.pack(fill=X)

        self.header_r5 = Label(self.row5, text="node_id", width=18)
        self.header_r5.pack(side=LEFT, padx=2, pady=5)

        self.entry_node_id = Entry(self.row5)
        self.entry_node_id.pack(fill=X, padx=2, expand=True)
        self.entry_node_id.bind('<Return>', self.connect_node_id)
        self.entry_node_id['state'] = 'disabled'

        # Строка №6
        self.row6 = Frame(self)
        self.row6.pack(fill=X)

        self.btn_check_map = Button(self.row6, text='Проверить подвязку', command=self.check_linking_from_SinLib)
        self.btn_check_map.pack(side=RIGHT, padx=2, pady=5)

        # self.btn_check_omx = Button(self.row6, text='Получить объекты', command=self.get_object_from_SinLib)
        self.btn_check_omx = Button(self.row6, text='Получить объекты', command=self.get_obj)
        self.btn_check_omx.pack(side=RIGHT, padx=2, pady=5)

        self.btn_link = Button(self.row6, text='Связать несвязанное', command=self.start_linking)
        self.btn_link.pack(side=RIGHT, padx=2, pady=5)

        self.btn_insert_to_cb = Button(self.row6, text='Показать объекты', command=self.get_obj_in_iosApp)
        self.btn_insert_to_cb.pack(side=RIGHT, padx=2, pady=5)
            
        """

    # Раскладываем все формы по рядам
    def __packing(self):
        for obj in self.fields.values():
            obj.pack(anchor=tk.W, padx=5, pady=3, fill=tk.X)

    # Выбор OMX файла
    def select_omx_file(self):
        filename = fd.askopenfilename(title='Open a file', initialdir=os.getcwd(), filetypes=[('All files', '*.omx')])
        self.fields['omx'].setNewTxt(filename)
        # self.entry_omx_path.delete(0, END)
        # self.entry_omx_path.insert(0, filename)
        self.myOmx = OmxFile(omx_path=filename)

        # if self.fields['omx'].getText() is not None:
        self.get_obj_in_iosApp()


    # Получаем список объектов в директории SinLib
    # def get_object_from_SinLib(self):
    #     if isinstance(self.myOmx, OmxFile):
    #         # self.clear_st()
    #         self.fields['log'].setNewTxt("Путь поиска: AstraRegul => IOS_App => SinLib\n")
    #         cnt = 0
    #         for i in self.myOmx.get_SinLib_struct():
    #             cnt += 1
    #             self.fields['log'].setNewTxt(f'{cnt}.Имя: {i:<10} Тип: {self.myOmx.get_Obj_base_type(i)}')

    # Получаем список объектов в выбранной комбобоксами папке
    # def get_object(self, iosObj, iosObjType):
    #     pass

    # Вставка в ST
    # def insert_to_st(self, text):
    #     self.st_omx_obj.configure(state='normal')
    #     self.st_omx_obj.insert(tk.INSERT, text + '\n')
    #     self.st_omx_obj.configure(state='disabled')

    # Очистить scrolled text
    # def clear_st(self):
    #     self.st_omx_obj.configure(state='normal')
    #     self.st_omx_obj.delete('1.0', END)
    #     self.st_omx_obj.configure(state='disabled')

    # Вставка в node_path
    # def insert_to_node_path(self, text):
    #     self.entry_node_path.configure(state='normal')
    #     self.entry_node_path.delete(0, END)
    #     self.entry_node_path.insert(tk.INSERT, text)
    #     self.entry_node_path.configure(state='disabled')

    # Вставка в node_id
    # def insert_to_node_id(self, text):
    #     self.entry_node_id.configure(state='normal')
    #     self.entry_node_id.delete(0, END)
    #     self.entry_node_id.insert(tk.INSERT, text)
    #     self.entry_node_id.configure(state='disabled')

    # Выбор файла с картой
    def select_map_file(self):
        filename = fd.askopenfilename(title='Open a file', initialdir=os.getcwd(), filetypes=[('All files', '*.xml')])
        self.fields['map'].setNewTxt(filename)
        self.myMap = MapFile(map_path=filename)
        self.get_obj_in_iosApp()

    # Получаем список объектов в директории SinLib
    # def check_linking_from_SinLib(self):
    #     if isinstance(self.myMap, MapFile) and isinstance(self.myOmx, OmxFile):
    #         self.clear_st()
    #         self.insert_to_st("Путь поиска: AstraRegul => IOS_App => SinLib, подвязки\n")
    #         cnt = 0
    #         for i in self.myOmx.get_SinLib_struct():
    #             cnt += 1
    #             self.insert_to_st(
    #                 f'{cnt}.Имя: {i:<10} Тип: {self.myOmx.get_Obj_base_type(i)}'
    #                 f'{"Статус подвязки:":>20}{self.myMap.check_linking(i)}'
    #             )

    # Проверяем подвязку по выбранной карте
    def checkLinking(self):
        self.fields['log'].clear()
        self.fields['table'].clear()
        iosApp = self.fields['iosObj'].getValue()
        iosAppType = self.fields['iosType'].getValue()
        cnt = 0
        for i in self.myOmx.get_objName(iosApp, iosAppType):
            cnt += 1
            self.fields['log'].setNewTxt(f'{cnt}.Имя: {i:<10} Тип: {self.myOmx.get_base_type(iosApp, iosAppType, i)} '
                                         f'Библиотека: {self.myOmx.get_lib_name(iosApp, iosAppType, i)} '
                                         f'Подвязка: {self.myMap.checkLink(iosApp, iosAppType, i)}')

            self.fields['table'].insert(cnt, i, self.myOmx.get_base_type(iosApp, iosAppType, i),
                                        self.myOmx.get_lib_name(iosApp, iosAppType, i),
                                        self.myMap.checkLink(iosApp, iosAppType, i))


    # сохранить тег в файл
    def save_map(self):
        self.myMap.write_XML_to_map()

    # Установить значение переменной node_path_tag при нажатии Enter в поле ввода entry_node_path
    def connect_node_path(self, event):
        node_path_tag.set(self.fields['nodePath'].getValue())
        self.fields['nodePath'].clear()

    # Установить значение переменной node_path_tag при нажатии Enter в поле ввода entry_node_path
    def connect_node_id(self, event):
        node_id_tag.set(self.fields['nodeId'].getValue())
        self.fields['nodeId'].clear()

    # Связвание объектов
    def start_linking(self):

        global linkink_object

        self.fields['log'].clear()
        self.fields['log'].setNewTxt('Связывание')

        # self.btn_link['text'] = 'Связывание'
        # self.clear_st()

        iosApp = self.fields['iosObj'].getValue()
        iosAppType = self.fields['iosType'].getValue()

        for i in self.myOmx.get_objName(iosApp, iosAppType):
            if not self.myMap.checkLink(iosApp, iosAppType, i):

                print(i, self.myMap.checkLink(iosApp, iosAppType, i), self.myOmx.get_lib_name(iosApp, iosAppType, i))
                if self.myOmx.get_lib_name(iosApp, iosAppType, i) == 'SineticLib':

                    if iosAppType == 'AI' or iosAppType == 'AI1':
                        linkink_object = SinLib.AI(self.get_node_path(iosApp, iosAppType, i), self.get_node_id(iosApp, iosAppType, i))

                    if iosAppType == 'FC_CTRL':
                        linkink_object = SinLib.FC_CTRL(self.get_node_path(iosApp, iosAppType, i), self.get_node_id(iosApp, iosAppType, i))

                    for j in range(linkink_object.loopCnt()):
                        xmlObj = self.myMap.create_XMLtag(linkink_object[j][0],
                                                          linkink_object[j][1])  # создаем объект тега
                        self.myMap.insert_XML_to_map(xmlObj)  # вставляем объект в карту

        # # Для каждого объекта в IOs_App проверить подвязку
        # for i in self.myOmx.get_SinLib_struct():
        #     if not self.myMap.check_linking(i):
        #         # Проверяем на принадлежность библиотеке
        #         if self.myOmx.get_Obj_library_type(i) == 'SineticLib':
        #
        #             # Проверка на принадлежность типу DI библиотеке SineticLib
        #             if self.myOmx.get_Obj_base_type(i) == 'DI1':
        #                 linkink_object = SinLib.DI(self.get_node_path(i), self.get_node_id(i))
        #
        #             # AI
        #             if self.myOmx.get_Obj_base_type(i) == 'AI1':
        #                 linkink_object = SinLib.AI(self.get_node_path(i), self.get_node_id(i))
        #
        #             # VLVD
        #             if self.myOmx.get_Obj_base_type(i) == 'VLV_D':
        #                 linkink_object = SinLib.VLVD(self.get_node_path(i), self.get_node_id(i))
        #
        #             # VLVA
        #             if self.myOmx.get_Obj_base_type(i) == 'VLV_A':
        #                 linkink_object = SinLib.VLVA(self.get_node_path(i), self.get_node_id(i))
        #
        #             # MTR
        #             if self.myOmx.get_Obj_base_type(i) == 'MTR':
        #                 linkink_object = SinLib.MTR(self.get_node_path(i), self.get_node_id(i))
        #
        #             # PID
        #             if self.myOmx.get_Obj_base_type(i) == 'PID_A':
        #                 linkink_object = SinLib.PID(self.get_node_path(i), self.get_node_id(i))
        #
        #             for j in range(linkink_object.loopCnt()):
        #                 xmlObj = self.myMap.create_XMLtag(linkink_object[j][0],
        #                                                   linkink_object[j][1])  # создаем объект тега
        #                 self.myMap.insert_XML_to_map(xmlObj)  # вставляем объект в карту

        # self.btn_link['text'] = 'Связать несвязанное'
        # self.header_r3['text'] = ''
        self.save_map()  # сохраняем файл
        self.fields['log'].setNewTxt('Карта подвязки успешно обновлена')

    # Получить node-path объекта по имени и произвести процедуры с полем ввода
    def get_node_path(self, iosAppObj, iosAppObjType, obj_name):

        print('Hello')

        # Ждем ввода в поле node_path, подставляем туда node_path из свойства объекта
        self.fields['log'].setNewTxt(f'Связать {obj_name} подтверди node_path <ENTER>')

        self.fields['nodePath'].setNewTxt(self.myOmx.get_node_path(iosAppObj, iosAppObjType, obj_name))
        # self.insert_to_node_path(self.myOmx.get_Obj_node_path(object_name))  # Вставляем в поле путь до объекта

        self.fields['nodePath'].enable()
        self.fields['nodePath'].setFocus()
        # self.entry_node_path.configure(state='normal')  # активируем поле для ввода
        # self.entry_node_path.focus_set()  # устанавливаем курсор в поле

        root.wait_variable(node_path_tag)  # ждем ввода значения и нажатия Enter в поле
        node_path = node_path_tag.get()  # Получаем значения поля после нажатия кнопки Enter

        self.fields['nodePath'].disable()
        # self.entry_node_path.configure(state='disabled')  # деактивируем поле
        self.fields['log'].setNewTxt(f'Типу: {obj_name} присвоен node_path: {node_path}')

        return node_path

    # Аналогично получаем node_id
    def get_node_id(self, iosAppObj, iosAppObjType, obj_name):
        # self.header_r3[
        #     'text'] = f'Связать {object_name} Тип: {self.myOmx.get_Obj_base_type(object_name)}, подтверди node_id <ENTER>'

        self.fields['nodeId'].setNewTxt(self.myOmx.get_node_id(iosAppObj, iosAppObjType, obj_name))
        # self.insert_to_node_id(self.myOmx.get_Obj_node_id(object_name))

        self.fields['nodeId'].enable()
        self.fields['nodeId'].setFocus()
        # self.entry_node_id.configure(state='normal')
        # self.entry_node_id.focus_set()  # устанавливаем курсор в поле
        root.wait_variable(node_id_tag)  # ждем ввода значения и нажатия Enter в поле
        node_id = node_id_tag.get()

        self.fields['nodeId'].disable()
        # self.entry_node_id.configure(state='disabled')

        self.fields['log'].setNewTxt(f'Типу: {obj_name} присвоен node_id: {node_id}')
        # self.insert_to_st(f'Типу: {self.myOmx.get_Obj_base_type(object_name)} присвоен node_id: {node_id}')

        return node_id

    # Заполняем комбобокс сущетсвующими папками с типами (AI, DI и т.д.)
    def selected_iosApp(self, event):
        self.fields['iosType'].setValues(self.myOmx.get_types_in_iosApp(self.fields['iosObj'].getValue()))

    # Заполняем комбобокс объектами из IosApp
    def get_obj_in_iosApp(self):
        # Проверка на выбранный файлы OMX и MAP
        if len(self.fields['omx'].getText()) != 0 and len(self.fields['map'].getText()) != 0:
            self.fields['iosObj'].setValues(self.myOmx.get_objects_iosApp())
            self.selected_iosApp(0)


    # Получить список объектов внутри папки
    def get_obj(self):
        iosApp = self.fields['iosObj'].getValue()
        iosAppType = self.fields['iosType'].getValue()
        self.fields['table'].clear()
        cnt = 0
        for i in self.myOmx.get_objName(iosApp, iosAppType):
            cnt += 1
            self.fields['log'].setNewTxt(f'{cnt}.Имя: {i:<10} Тип: {self.myOmx.get_base_type(iosApp, iosAppType, i)} '
                                         f'Библиотека: {self.myOmx.get_lib_name(iosApp, iosAppType, i)}')

            self.fields['table'].insert(cnt, i, self.myOmx.get_base_type(iosApp, iosAppType, i), self.myOmx.get_lib_name(iosApp, iosAppType, i), None)


if __name__ == '__main__':
    root = Tk()
    node_path_tag = tk.StringVar()  # тег ПЛК
    node_id_tag = tk.StringVar()  # тег ПЛК
    root.geometry("640x510")
    app = MapLinker()
    root.mainloop()
    #HelloMax
