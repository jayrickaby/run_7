import platform

from PySide6.QtCore import QObject, Property
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "jayrickaby.run7.system"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class System(QObject):

    @Property(str, constant=True)
    def simpleOsName(self):
        name = platform.system()

        if name == "Darwin":
            return "macOS"

        return name