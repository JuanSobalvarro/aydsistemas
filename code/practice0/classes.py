import datetime
import enum

class Modality(enum.Enum):
    diario = "Diario"
    sabatino = "Sabatino"

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


class Student(Person):
    def __init__(self, card: str, name: str, birthdate: datetime.date):
        super().__init__(name, birthdate)

        self.card = card

    @property
    def greet(self):
        return f"Soy el alumno {self.name}, tengo {self.age}"


class Professor(Person):

    def __init__(self, professorID: str, name: str, birthdate: datetime.date, title: str, headship: str, contractType: str):
        super().__init__(name, birthdate)

        self.professorID = professorID
        self.title = title
        self.headship = headship
        self.contractType = self.__setContract(contractType)

    @staticmethod
    def __setContract(contractType: str):
        if contractType not in ['planta', 'horario']:
            raise ValueError
        return contractType

    @property
    def greet(self):
        return f"Soy el profesor {self.name}, tengo {self.age} y soy de {self.contractType}"


class Subject:
    def __init__(self, subjectID: str, name: str, credit: int):
        
        self.subjectID = subjectID
        self.name = name
        self.credit = credit


class Course:

    def __init__(self, courseID: str, cycle: str, modality: Modality, professor: Professor, subject: Subject):

        self.courseID = courseID
        self.cycle = cycle
        self.modality = modality.name
        self.professor = professor
        self.subject = subject
        self.students: list[Student] = []
        self.__notes: dict[Student, float] = {}

    def addStudent(self, student: Student) -> bool:

        if student not in self.students:
            self.students.append(student)
            return True

        return False

    def removeStudent(self, student: Student) -> bool:

        if student in self.students:
            self.students.remove(student)
            return True

        return False

    def addNote(self, student: Student, note: float) -> bool:

        if student in self.students:
            self.__notes[student] = note
            return True

        return False

    def getNotes(self) -> dict[Student, float]:

        return self.__notes
