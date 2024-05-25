import classes
from faker import Faker

fake = Faker('es_ES')


def randomStudentsList(numOfStudents: int) -> list[classes.Student]:
    students = []

    for i in range(numOfStudents):

        students.append(classes.Student(f"{i}", f"{fake.first_name()} {fake.last_name()}", fake.date_between('-24y', '-16y')))

    return students

