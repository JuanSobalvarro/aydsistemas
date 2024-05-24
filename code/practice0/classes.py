import datetime


class Person:

    def __init__(self, name: str, birthdate: datetime.date):
        self.name = name
        self.birthdate = birthdate
        self.age = self.__getAge()

    def __getAge(self):
        today = datetime.date.today()
        return today.year - self.birthdate.year

    @property
    def greet(self):
        return f"Hola soy {self.name} y tengo {self.age}"


class Alumn(Person):
    def __init__(self, name: str, birthdate: datetime.date, carnet):
        super().__init__(name, birthdate)

        self.carnet = carnet

    @property
    def greet(self):
        return f"Soy el alumno {self.name}, tengo {self.age}"


class Professor(Person):

    def __init__(self, name: str, birthdate: datetime.date, contractType: str):
        super().__init__(name, birthdate)

        self.contractType = self.__setContract(contractType)

    @staticmethod
    def __setContract(contractType: str):
        if contractType not in ['planta', 'horario']:
            raise ValueError
        return contractType

    @property
    def greet(self):
        return f"Soy el profesor {self.name}, tengo {self.age} y soy de {self.contractType}"


class Course:
    def __init__(self):
        pass


class Assignment:
    def __init__(self):
        pass
