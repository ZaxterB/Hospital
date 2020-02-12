from PyQt5.QtWidgets import *
import datetime

class Staff:
    def __init__(self, name: str, email: str ):
        self.name = name
        self.email = email


class OnCallStaff(Staff):
    def __init__(self, name: str, email: str, sms: int):
        super().__init__(name, email)
        self. sms = sms


class OnCallPeriod:
    def __init__(self, start: datetime.datetime, staff: Staff):
        self.start = start
        self.staff = staff


class Monitortype:
    def __init__(self, name: str):
        self.name = name
        values = self.get_values(name)
        self.unit = values['unit']
        self.min = values['defaultmin']
        self.max = values['defaultmax']
        self.dangermin = values['dangermin']
        self.dangermax = values['dangermax']

    def get_values(self, name) -> dict:
        #TODO get monitortypes & values from database
        return {
            'unit': 'PLACEHOLDERunit',
            'defaultmin': 'PLACEHOLDERdefaultmin',
            'defaultmax': 'PLACEHOLDERdefaultmax',
            'dangermin': 'PLACEHOLDERdangermin',
            'dangermax': 'PLACEHOLDERdangermax'
        }



class Module:
    def __init__(self):
        raise NotImplementedError()


class Bed:
    def __init__(self):
        raise NotImplementedError()


class Patient:
    def __init__(self, name: str):
        self.name = name


class CentralStation:
    def __init__(self):
        self.staff = []
        self.beds = []

    def register_staff(self, staff: Staff) -> None:
        raise NotImplementedError()

    def deregister_staff(self, staff: Staff) -> None:
        raise NotImplementedError()

    def register_bed(self, bed: Bed) -> None:
        raise NotImplementedError()

    def deregister_bed(self, bed: Bed) -> None:
        raise NotImplementedError()

    def receive_status(self) -> None:
        raise NotImplementedError()



if __name__ == "__main__":
    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()
    label2 = QLabel('I am a stegosaurus!')
    label2.show()
    app.exec_()