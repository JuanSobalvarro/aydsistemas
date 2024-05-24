import datetime
import classes
import pytest


def test0():
    x = datetime.datetime(2004, 8, 23)
    uwu = classes.Person("Juan", x)
    print(uwu.greet)

def test1():
    x = datetime.datetime(2004, 8, 23)
    uwu = classes.Professor("Juan", x, "horario")
    print(uwu.greet)

    assert uwu.greet == "Soy el profesor Juan, tengo 20 y soy de horario"