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


# class BaseObj:
#     def __init__(self, node_path, node_id):
#         self.tag_lst = None
#         self.node_path = node_path
#         self.node_id = node_id
#
#     # Получение значения в цикле
#     def __getitem__(self, key):
#         if key < len(self.tag_lst):
#             return self.tag_lst[key]
#
#     # Длина списка
#     def loopCnt(self):
#         return len(self.tag_lst)


#
# class PID(BaseObj):
#     def __init__(self, plc_tag):
#         super().__init__(plc_tag)
#         self.tag_lst = [
#             f'Application.{self.tag}.sPID.SpMin',
#             f'Application.{self.tag}.sPID.SpMax',
#             f'Application.{self.tag}.sPID.ErrMin',
#             f'Application.{self.tag}.sPID.ErrMax',
#             f'Application.{self.tag}.sPID.Tf',
#             f'Application.{self.tag}.sPID.MvMin',
#             f'Application.{self.tag}.sPID.MvMax',
#             f'Application.{self.tag}.sPID.PvMin',
#             f'Application.{self.tag}.sPID.PvMax',
#             f'Application.{self.tag}.sPID.K',
#             f'Application.{self.tag}.sPID.Ti',
#             f'Application.{self.tag}.sPID.Td',
#             f'Application.{self.tag}.sPID.SpMode',
#             f'Application.{self.tag}.sPID.SpLoc',
#             f'Application.{self.tag}.sPID.ManMode',
#             f'Application.{self.tag}.sPID.MvMan',
#             f'Application.{self.tag}.sPID.Diagn',
#             f'Application.{self.tag}.sPID.Mv',
#             f'Application.{self.tag}.sPID.SpOn',
#             f'Application.{self.tag}.sPID.SpFact',
#             f'Application.{self.tag}.sPID.Mode',
#             f'Application.{self.tag}.sPID.SpOut.VALUE',
#             f'Application.{self.tag}.sPID.SpOut.QUALITY',
#             f'Application.{self.tag}.sPID.Err.VALUE',
#             f'Application.{self.tag}.sPID.Err.QUALITY',
#             f'Application.{self.tag}.sPID.Pv.VALUE',
#             f'Application.{self.tag}.sPID.Pv.QUALITY',
#             f'Application.{self.tag}.sPID.Balance',
#             f'Application.{self.tag}.sPID.MsgOff'
#         ]
#
#
# class MTR(BaseObj):
#     def __init__(self, plc_tag):
#         super().__init__(plc_tag)
#         self.tag_lst = [
#             f'Application.{self.tag}.sMtr.HmiCmd',
#             f'Application.{self.tag}.sMtr.Diagn',
#             f'Application.{self.tag}.sMtr.Mode',
#             f'Application.{self.tag}.sMtr.RqstW',
#             f'Application.{self.tag}.sMtr.CtlW',
#             f'Application.{self.tag}.sMtr.HmiBlock',
#             f'Application.{self.tag}.sMtr.Block',
#             f'Application.{self.tag}.sMtr.State',
#             f'Application.{self.tag}.sMtr.Worktime',
#             f'Application.{self.tag}.sMtr.sCurrent.VALUE',
#             f'Application.{self.tag}.sMtr.sCurrent.QUALITY',
#             f'Application.{self.tag}.sMtr.Imit',
#             f'Application.{self.tag}.sMtr.MsgOff',
#             f'Application.{self.tag}.sMtr.SetMode',
#             f'Application.{self.tag}.sMtr.sFreq.VALUE',
#             f'Application.{self.tag}.sMtr.sFreq.QUALITY',
#             f'Application.{self.tag}.sMtr.InterlockSet'
#         ]
#
#
# class VLVD(BaseObj):
#     def __init__(self, plc_tag):
#         super().__init__(plc_tag)
#         self.tag_lst = [
#             f'Application.{self.tag}.sVlv.OpnTime',
#             f'Application.{self.tag}.sVlv.ClsTime',
#             f'Application.{self.tag}.sVlv.SetMode',
#             f'Application.{self.tag}.sVlv.HmiCmd',
#             f'Application.{self.tag}.sVlv.Diagn',
#             f'Application.{self.tag}.sVlv.Mode',
#             f'Application.{self.tag}.sVlv.RqstW',
#             f'Application.{self.tag}.sVlv.CtlW',
#             f'Application.{self.tag}.sVlv.HmiBlock',
#             f'Application.{self.tag}.sVlv.Block',
#             f'Application.{self.tag}.sVlv.State',
#             f'Application.{self.tag}.sVlv.TimeOut',
#             f'Application.{self.tag}.sVlv.Imit',
#             f'Application.{self.tag}.sVlv.MsgOff',
#             f'Application.{self.tag}.sVlv.InterlockSet'
#         ]
#
#
# class VLVA(BaseObj):
#     def __init__(self, plc_tag):
#         super().__init__(plc_tag)
#         self.tag_lst = [
#             f'Application.{self.tag}.sVlv.sConfig.RUNTIME',
#             f'Application.{self.tag}.sVlv.MvMan',
#             f'Application.{self.tag}.sVlv.SetMode',
#             f'Application.{self.tag}.sVlv.HmiCmd',
#             f'Application.{self.tag}.sVlv.Diagn',
#             f'Application.{self.tag}.sVlv.Mode',
#             f'Application.{self.tag}.sVlv.RqstW',
#             f'Application.{self.tag}.sVlv.HmiBlock',
#             f'Application.{self.tag}.sVlv.Block',
#             f'Application.{self.tag}.sVlv.State',
#             f'Application.{self.tag}.sVlv.Mv',
#             f'Application.{self.tag}.sVlv.Inh',
#             f'Application.{self.tag}.sVlv.sPos.VALUE',
#             f'Application.{self.tag}.sVlv.sPos.STATUS',
#             f'Application.{self.tag}.sVlv.Imit',
#             f'Application.{self.tag}.sVlv.MsgOff',
#             f'Application.{self.tag}.sVlv.InterlockSet'
#         ]
#

# class DI(BaseObj):
#     def __init__(self, node_path, node_id):
#         super().__init__(node_path, node_id)
#         # Вложенный список с Node_path и node_id для создания объектов XML
#         # 0 - путь к объекту по вложенным папкам в AStudio (SinLib.di.MSG_OFF)
#         # 1 - путь тегу в OPCUA ПЛК (Application.DI_DI1.sDI.MsgOff)
#         self.tag_lst = [
#             [f'{self.node_path}.INV_ON', f'Application.{self.node_id}.sDI.Inv'],
#             [f'{self.node_path}.MODE', f'Application.{self.node_id}.sDI.Mode'],
#             [f'{self.node_path}.IMIT_VALUE', f'Application.{self.node_id}.sDI.ImitValue'],
#             [f'{self.node_path}.OUT.VALUE', f'Application.{self.node_id}.sDI.Out.VALUE'],
#             [f'{self.node_path}.OUT.QUALITY', f'Application.{self.node_id}.sDI.Out.QUALITY'],
#             [f'{self.node_path}.DIAGN', f'Application.{self.node_id}.sDI.Diagn'],
#             [f'{self.node_path}.FLT_EN', f'Application.{self.node_id}.sDI.EnFlt'],
#             [f'{self.node_path}.FLT_TM', f'Application.{self.node_id}.sDI.FltrTime'],
#             [f'{self.node_path}.MSG_OFF', f'Application.{self.node_id}.sDI.MsgOff'],
#             [f'{self.node_path}.IMIT', f'Application.{self.node_id}.sDI.Imit'],
#             [f'{self.node_path}.RAW', f'Application.{self.node_id}.sDI.RAW']
#         ]


#
# class AI(BaseObj):
#     def __init__(self, plc_tag):
#         super().__init__(plc_tag)
#         self.tag_lst = [
#             f'Application.{self.tag}.sAI.Ymin',
#             f'Application.{self.tag}.sAI.Ymax',
#             f'Application.{self.tag}.sAI.Ah',
#             f'Application.{self.tag}.sAI.Wh',
#             f'Application.{self.tag}.sAI.Wl',
#             f'Application.{self.tag}.sAI.Al',
#             f'Application.{self.tag}.sAI.Tf',
#             f'Application.{self.tag}.sAI.Hyst',
#             f'Application.{self.tag}.sAI.SignCheck',
#             f'Application.{self.tag}.sAI.Ah2',
#             f'Application.{self.tag}.sAI.Al2',
#             f'Application.{self.tag}.sAI.Out.VALUE',
#             f'Application.{self.tag}.sAI.Out.QUALITY',
#             f'Application.{self.tag}.sAI.Imit',
#             f'Application.{self.tag}.sAI.ImitValue',
#             f'Application.{self.tag}.sAI.FactValue',
#             f'Application.{self.tag}.sAI.Sign',
#             f'Application.{self.tag}.sAI.Mode',
#             f'Application.{self.tag}.sAI.Diagn',
#             f'Application.{self.tag}.sAI.MsgOff',
#             f'Application.{self.tag}.sAI.LimitCheck'
#         ]
#
#

# class OmxFile:
#     def __init__(self, omx_path='Li.omx'):
#         self.omx_path = omx_path
#         self.tree = ET.parse(omx_path)
#         self.omx = self.tree.getroot()
#
#     # Получение списка имен объектов в AstraRegul => IOS_App => SinLib
#     def get_SinLib_struct(self):
#         # рабочая ветка
#         sinLibLst = []
#         AstraRegul = self.omx.find('{automation.deployment}domain')
#         IosApp = AstraRegul.find('{automation.deployment}application-object')
#         for logicObj in IosApp:
#             if logicObj.get('name') == 'SinLib':
#                 for obj in logicObj:
#                     sinLibLst.append(obj.get('name'))
#
#         return sinLibLst
#
#     # Получить тип объекта в директории SinLib
#     def get_Obj_base_type(self, obj_name):
#         AstraRegul = self.omx.find('{automation.deployment}domain')
#         IosApp = AstraRegul.find('{automation.deployment}application-object')
#         for logicObj in IosApp:
#             if logicObj.get('name') == 'SinLib':
#                 for obj in logicObj:
#                     if obj.get('name') == obj_name:
#                         return obj.get('base-type').split('.')[-2]
#
#         return None
#
#     # Получить путь объекта по имени в директории SinLib
#     def get_Obj_node_path(self, obj_name):
#         AstraRegul = self.omx.find('{automation.deployment}domain')
#         IosApp = AstraRegul.find('{automation.deployment}application-object')
#         for logicObj in IosApp:
#             if logicObj.get('name') == 'SinLib':
#                 for obj in logicObj:
#                     if obj.get('name') == obj_name:
#                         return '.'.join(obj.get('original').split('.')[
#                                         3:])  # Возвращаем путь после 'REGUL_R500_51_1_A', 'Runtime', 'SDM_app'
#
#         return None


# class MapFile:
#     def __init__(self, map_path='SDM_app_map.xml'):
#         self.path = map_path
#         self.tree = ET.parse(self.path)
#         self.file = self.tree.getroot()
#
#         self.test_path = 'test.xml'
#         self.test_tree = ET.parse(self.test_path)
#         self.test_file = self.test_tree.getroot()
#
#     # Получение списка тегов в карте для папки SinLib
#     def get_link_for_SinLib(self):
#         linkObj = []
#         # Все что в карте адресов с из папки SinLib
#         for child in self.file.findall('item'):
#             node_path = child.find('node-path').text
#             if node_path.find('SinLib') != -1:
#                 linkObj.append(node_path)
#
#         return linkObj
#
#     # Проверка objName на хотябы одну запись в карте адресов для папки SinLib
#     def check_linking(self, objName):
#         linkObj = []
#         # Все что в карте адресов с из папки SinLib
#         for child in self.file.findall('item'):
#             node_path = child.find('node-path').text
#             if node_path.find('SinLib') != -1 and node_path.find(objName) != -1:
#                 return True  # Есть привязка
#
#         return False  # Нет привязки
#
#     # Процесс вставки XML структуры тега в карту подвязки адресов
#     # def start_linking(self, objName):
#
#     # Создаем структуру тега в XML виде
#     # node_path - путь к тегу в AStudio, например SinLib.mtr1.HMI_CMD
#     # node_id - путь к тегу в OPC (UAExpert), например Application.MTR_MTR1.sMtr.HmiCmd
#     def create_XMLtag(self, node_path, node_id):
#
#         newObj = ET.Element('item', Binding='Introduced')
#         ET.indent(newObj, space='   ', level=0)
#
#         tagStruct = {
#             'node-path': node_path,
#             'namespace': 'urn:ProsoftSystems:regul_ua_server:iec_data',
#             'nodeIdType': 'String',
#             'nodeId': node_id,
#         }
#
#         for key, value in tagStruct.items():
#             ET.SubElement(newObj, key).text = value
#             ET.indent(newObj, space='   ', level=1)
#
#         # ET.dump(newObj)
#         return newObj
#
#     # Вставка объекта объекат xmlObj в файл
#     def insert_XML_to_map(self, xmlObj):
#         self.test_file.insert(len(self.test_file), xmlObj)
#
#         # return file
#         # ET.dump(self.test_file)
#
#     def write_XML_to_map(self):
#
#         for i in range(len(self.test_file)):
#             ET.indent(self.test_file, space='\t', level=0)  # приводим в порядок XML отображение
#
#         # ET.dump(self.test_file)
#         self.test_tree.write('test.xml')
#         print("Запись в файл")


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

        # self.btn_test = Button(self.row6, text='Тест', command=self.test_func)
        # self.btn_test.pack(side=RIGHT, padx=2, pady=5)

        # self.image = tk.PhotoImage(file="sin_logo.png")
        # self.label = ttk.Label(image=self.image)
        # self.label.pack(padx=2, pady=5)

        # Load an image in the script
        # self.img = (Image.open("sin_logo.png"))

        # Resize the Image using resize method
        # self.resized_image = self.img.resize((400, 100))
        # self.new_image = ImageTk.PhotoImage(self.resized_image)
        # self.label = ttk.Label(image=self.new_image)
        # self.label.pack(padx=2, pady=5)


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
'''
    # Получить спсиок объектов в папке SinLib в IOS_APP
    myOmx = OmxFile()
    print(myOmx.__dict__)
    print(*myOmx.get_SinLib_struct(), sep='\n')

    # Получить все подвязки для объектов в папке SinLib
    myMap = MapFile()
    print(myMap.__dict__)
    print(*myMap.get_link_for_SinLib(), sep='\n')

    # Для каждого объекта в IOs_App проверить подвязку
    for i in myOmx.get_SinLib_struct():
        # print(myOmx.get_Obj_base_type(i)) # получения типа объекта
        # print(i, myMap.check_linking(i)) # проверка на подвязку

        if not myMap.check_linking(i):
            if myOmx.get_Obj_base_type(i) == 'DI1':
                newDi = DI('SinLib.di', 'DI_DI1')

                for i in range(newDi.loopCnt()):
                    xmlObj = myMap.create_XMLtag(newDi[i][0], newDi[i][1])  # создаем объект тега
                    myMap.insert_XML_to_map(xmlObj)  # вставляем объект в карут

                myMap.write_XML_to_map()  # записываем карту в файл

            # print(myOmx.get_Obj_base_type(i))

    # myMap.create_XMLtag('123', '456')
    # myOmx.get_SinLib_struct()
'''
