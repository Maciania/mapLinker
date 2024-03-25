import xml.etree.ElementTree as ET


class MapFile:
    def __init__(self, map_path='SDM_app_map.xml'):
        self.path = map_path
        self.tree = ET.parse(self.path)
        self.file = self.tree.getroot()

    # Получение списка тегов в карте для папки SinLib
    def get_link_for_SinLib(self):
        linkObj = []
        # Все что в карте адресов с из папки SinLib
        for child in self.file.findall('item'):
            node_path = child.find('node-path').text
            if node_path.find('SinLib') != -1:
                linkObj.append(node_path)

        return linkObj

    # Проверка objName на хотябы одну запись в карте адресов для папки SinLib
    def check_linking(self, objName):
        linkObj = []
        # Все что в карте адресов с из папки SinLib
        for child in self.file.findall('item'):
            node_path = child.find('node-path').text
            if node_path.find('SinLib') != -1 and node_path.find(objName) != -1:
                return True  # Есть привязка

        return False  # Нет привязки


    # Создаем структуру тега в XML виде
    # node_path - путь к тегу в AStudio, например SinLib.mtr1.HMI_CMD
    # node_id - путь к тегу в OPC (UAExpert), например Application.MTR_MTR1.sMtr.HmiCmd
    def create_XMLtag(self, node_path, node_id):

        newObj = ET.Element('item', Binding='Introduced')
        ET.indent(newObj, space='   ', level=0)

        tagStruct = {
            'node-path': node_path,
            'namespace': 'urn:ProsoftSystems:regul_ua_server:iec_data',
            'nodeIdType': 'String',
            'nodeId': node_id,
        }

        for key, value in tagStruct.items():
            ET.SubElement(newObj, key).text = value
            ET.indent(newObj, space='   ', level=1)

        # ET.dump(newObj)
        return newObj

    # Вставка объекта объекат xmlObj в файл
    def insert_XML_to_map(self, xmlObj):
        self.file.insert(len(self.file), xmlObj)
        ET.indent(self.file, space='\t', level=0)

    def write_XML_to_map(self):
        self.tree.write(self.path)
        print("Запись в файл")
