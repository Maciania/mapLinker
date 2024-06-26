import xml.etree.ElementTree as ET


class OmxFile:
    def __init__(self, omx_path='Li.omx'):
        self.omx_path = omx_path
        self.tree = ET.parse(omx_path)
        self.omx = self.tree.getroot()

    # Получение списка имен объектов в AstraRegul => IOS_App => SinLib
    def get_SinLib_struct(self):
        # рабочая ветка
        sinLibLst = []
        AstraRegul = self.omx.find('{automation.deployment}domain')
        IosApp = AstraRegul.find('{automation.deployment}application-object')
        for logicObj in IosApp:
            if logicObj.get('name') == 'SinLib':
                for obj in logicObj:
                    sinLibLst.append(obj.get('name'))

        return sinLibLst

    # Получить тип объекта в директории SinLib
    def get_Obj_base_type(self, obj_name):
        AstraRegul = self.omx.find('{automation.deployment}domain')
        IosApp = AstraRegul.find('{automation.deployment}application-object')
        for logicObj in IosApp:
            if logicObj.get('name') == 'SinLib':
                for obj in logicObj:
                    if obj.get('name') == obj_name:
                        return obj.get('base-type').split('.')[-2]

        return None

    # Получить путь объекта по имени в директории SinLib
    def get_Obj_node_path(self, obj_name):
        AstraRegul = self.omx.find('{automation.deployment}domain')
        IosApp = AstraRegul.find('{automation.deployment}application-object')
        for logicObj in IosApp:
            if logicObj.get('name') == 'SinLib':
                for obj in logicObj:
                    if obj.get('name') == obj_name:
                        return '.'.join(obj.get('original').split('.')[
                                        3:])  # Возвращаем путь после 'REGUL_R500_51_1_A', 'Runtime', 'SDM_app'

        return None

    # Получить путь объекта по имени в директории SinLib
    def get_Obj_node_id(self, obj_name):
        AstraRegul = self.omx.find('{automation.deployment}domain')
        IosApp = AstraRegul.find('{automation.deployment}application-object')
        for logicObj in IosApp:
            if logicObj.get('name') == 'SinLib':
                for obj in logicObj:
                    if obj.get('name') == obj_name:
                        return obj.get('original').split('.')[-1]

        return None

    # Получить тип библиотеки из которой экземпляром которой является объект
    def get_Obj_library_type(self, obj_name):
        AstraRegul = self.omx.find('{automation.deployment}domain')
        IosApp = AstraRegul.find('{automation.deployment}application-object')
        for logicObj in IosApp:
            if logicObj.get('name') == 'SinLib':
                for obj in logicObj:
                    if obj.get('name') == obj_name:
                        return obj.get('base-type').split('.')[1]

        return None