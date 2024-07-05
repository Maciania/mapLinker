import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import Tk, Text, BOTH, X, N, LEFT, RIGHT, END
from tkinter.ttk import Frame, Label, Entry, Button

# Парсинг карты адресов
# tree = ET.parse('SDM_app_map.xml')
# root = ET.parse('SDM_app_map.xml').getroot()

# for child in root:
#     print(child.tag, child.attrib)

# рабочая ветка
# for child in root.findall('item'):
#     node_path = child.find('node-path').text
#     # if (node_path.find('SinLib') != -1 and node_path.find('di') != -1):
#     if node_path.find('SinLib') != -1:
#         print(node_path)

# Парсинг OMX файла проекта
# tree = ET.parse('Li.omx')
# omx = ET.parse('Li.omx').getroot()

# for child in root.findall('{automation.deployment}domain'):


# рабочая ветка
# AstraRegul = omx.find('{automation.deployment}domain')
# IosApp = AstraRegul.find('{automation.deployment}application-object')
# for logicObj in IosApp:
#     if logicObj.get('name') == 'SinLib':
#         for obj in logicObj:
#             print(obj.get('name'))  # Получение списка имен объектов в AstraRegul =>  IOS_App => SinLib

# for i in child.findall('{automation.deployment}application-object'):
#     name2 = i.find('{http://people.example.com}name')
#     name = i.get('name')
#     print(name)
# print("1")

#
# for child in root:
#     print(child.tag,"***", child.attrib)
#
#
# for neighbor in root.iter('{system}link-unit'):
#     print(neighbor.attrib)


# создаем свой объект (первый вариант создания XML струтктуры)
"""
newObj = ET.Element('item', Binding='TestBinding')
# ET.indent(newObj, space='   ', level=0)
ET.indent(newObj, space='   ', level=0)
# ET.indent(newObj, space='\t', level=0)

node_pt = ET.SubElement(newObj, 'node-path')
node_pt.text = '123-node-path'
ET.indent(newObj, space='   ', level=1)

namespace = ET.SubElement(newObj, 'namespace')
namespace.text = '123-namespace'
ET.indent(newObj, space='   ', level=1)

nodeIdType = ET.SubElement(newObj, 'nodeIdType')
nodeIdType.text = 'String'
ET.indent(newObj, space='   ', level=1)

nodeId = ET.SubElement(newObj, 'nodeId')
nodeId.text = 'Application.MTR_MTR1.sMtr.HmiCmd123'
ET.indent(newObj, space='   ', level=1)



# print(ET.tostring(newObj))
# ET.dump(newObj)

# второй вариант создания xml структуры
# newObj2 = ET.fromstring('<item Binding="Introduced">\n    '
#                         '<node-path>test</node-path>\n    '
#                         '<namespace>urn:ProsoftSystems:regul_ua_server:iec_data</namespace>\n    '
#                         '<nodeIdType>String</nodeIdType>\n    '
#                         '<nodeId>Application.MTR_MTR1.sMtr.HmiCmd123</nodeId>\n    '
#                         '</item>\n    ')
#
# ET.dump(newObj2)
# print(ET.tostring(newObj2))

# Парсинг карты
testTree = ET.parse('test.xml')
test = testTree.getroot()

# test = ET.parse('test.xml').getroot()
# print(ET.tostring(test))

# вставка дочерних элементов
for i in range(1):
    test.insert(len(test), newObj)
    ET.indent(test, space='\t', level=0) # приводим в порядок XML отображение

ET.dump(test)


# for i in test:
#     print(i.tag, i.attrib)
#     for j in i:
#         print(j.tag, i.find(str(j.tag)).text)
#
#     print('======================')


# test.insert(-1, newObj)

testTree.write('test.xml')

# ET.dump(test)


# Парсинг OMX файла проекта
tree = ET.parse('Li.omx')
omx = ET.parse('Li.omx').getroot()
# ET.dump(tree)

# Вывод всех папок в IosApp
AstraRegul = omx.find('{automation.deployment}domain')
IosApp = AstraRegul.find('{automation.deployment}application-object')

myLst = [logicObj.get('name') for logicObj in IosApp]
print(myLst)
# for logicObj in IosApp:
#     print(logicObj.get('name'), type(logicObj.get('name')))

for logicObj in IosApp:
    if logicObj.get('name') == 'SinLib':
        for obj in logicObj:
            ET.dump(obj)
            print(obj.get('name'))  # Получение списка имен объектов в AstraRegul =>  IOS_App => SinLib


# ET.dump(omx)

"""

root = tk.Tk()
root.title('Login')
root.geometry("400x300")


class MyFileDialog(Frame):
    """Класс с контейнером из трех элементов для выбора файла из директории проекта
    Используется для выбора файла проекта *omx и файла карты в который добавляются привязки"""

    def __init__(self, labelTxt, btnTxt, cmd, master=None):
        super().__init__(master)
        self.__init(labelTxt, btnTxt, cmd)

    def __init(self, labelTxt, btnTxt, cmd):
        self.label = Label(self, text=labelTxt)
        self.entry = Entry(self)
        self.btn = Button(self, text=btnTxt, command=cmd)
        self.__packing()

    def __packing(self):
        self.label.pack(side="left", padx=10)
        self.entry.pack(side="left", expand=True, fill=X)
        self.btn.pack(side="left", padx=10)


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
        self.entry.configure(state='normal')
        self.entry.delete(0, END)
        self.entry.insert(tk.INSERT, newText)
        self.entry.configure(state='disabled')


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
            btn.pack(side="left", padx=10, expand=True, fill=X)


def myPrint(*args):
    print('hello? max')


# print(myField(Label(text="Файл проекта OMX", width=18), Button(text='Открыть'), Entry()).__dict__)
# fields = {}
#
# fields['username_label'] = ttk.Label(text='Username:')
# fields['username'] = ttk.Entry()
#
# fields['password_label'] = ttk.Label(text='Password:')
# fields['password'] = ttk.Entry(show="*")
#
# fields['test'] = myFileDialog('hello', 'max')
#
# for field in fields.values():
#     field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
#
# ttk.Button(text='Login').pack(anchor=tk.W, padx=10, pady=5)
#

MyFileDialog('Файл проекта OMX :', 'Открыть', cmd=myPrint).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
MyFileDialog('Файл карты :', 'Открыть', cmd=myPrint).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
MyComboBox('Выбор1 :', bindCombo=myPrint).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
MyComboBox('Выбор2 :', bindCombo=myPrint).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
MyLabelFrame('NodePath :', bindEntry=myPrint).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
MyLabelFrame('NodeId :', bindEntry=myPrint).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
ControlField(('Раз', myPrint), ('Два', myPrint), ('Три', myPrint), ('Четыре', myPrint)).pack(anchor=tk.W, padx=10,
                                                                                             pady=5, fill=tk.X)
root.mainloop()
