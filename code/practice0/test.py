import datetime
import classes
import pytest
import utils
import numpy

def test0():
    x = datetime.datetime(2004, 8, 23)
    uwu = classes.Person("Juan", x)
    print(uwu.greet)

def test1():
    x = datetime.datetime(2004, 8, 23)
    uwu = classes.Professor("1", "Juan", x, "uwu", "uwu", "horario")
    print(uwu.greet)

    assert uwu.greet == "Soy el profesor Juan, tengo 20 y soy de horario"

def test2():

    students = utils.randomStudentsList(20)
    asignatura = classes.Subject("1", "Matematicas", 5)
    profesor = classes.Professor("1", "Juan", datetime.datetime(2004, 8, 23), "Ingeniero", "Jefe de Carrera", "planta")

    course = classes.Course("1", "1.er Cuatrimestre", "diario", profesor, asignatura)

    notes = numpy.random.normal(85, 15, 20)

    for student, note in zip(students, numpy.clip(notes, 0, 100)):
        course.addStudent(student)
        course.addNote(student, note)

    sizecourse = len(course.getNotes())

    print(profesor.greet + " y mis estudiantes son: ")
    for student in students:
        print(student.greet + " mis nota es: " + "%.2f" % course.getNotes()[student])

    assert sizecourse == 20