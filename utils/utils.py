from random import randint
import datetime

def getSpVatNumber():

    _letters = ("T","R","W","A","G","M","Y","F","P","D","X","B",
                        "N","J","Z","S","Q","V","H","L","C","K","E","T",)
    _VatNumber = randint(10000000, 99999999)
    _ExtNumber = randint(20, 70)
    _VatLetter = _letters[_VatNumber % 23]
    return str(_ExtNumber) + str(_VatNumber) + _VatLetter

def getSpMobileNumber():
    _MobileNumber = randint(10000000, 99999999)
    _ExtNumber = randint(610, 699)
    return str(_ExtNumber) + str(_MobileNumber)

def getSpEmail(nombre, apellido1, apellido2):
    _Email = nombre[0] +  apellido1.replace(' ', '') + apellido2[0] + "@freeemail.com"
    return _Email

def getRandomDate():
    _year = randint(1940, 2022)
    _month = randint(1, 12)
    if _month == 1:
        _day = randint(1, 31)
    elif _month == 2:
        _day = randint(1, 28)
    elif _month == 3:
        _day = randint(1, 31)
    elif _month == 4:
        _day = randint(1, 30)
    elif _month == 5:
        _day = randint(1, 31)
    elif _month == 6:
        _day = randint(1, 30)
    elif _month == 7:
        _day = randint(1, 31)
    elif _month == 8:
        _day = randint(1, 31)
    elif _month == 9:
        _day = randint(1, 30)
    elif _month == 10:
        _day = randint(1, 31)
    elif _month == 11:
        _day = randint(1, 30)
    elif _month == 12:
        _day = randint(1, 31)
    else:
        _day = 1

    return datetime.datetime(_year, _month, _day)

