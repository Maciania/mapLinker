import xml.etree.ElementTree as ET

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