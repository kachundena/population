import datetime
import sys
from multiprocessing import Process

sys.path.insert(0, './model')
sys.path.insert(0, './utils')

from database import *
from lists import *
from stats import *
from utils import *

from person import *


        #personas = []
def createpersons(elements):
    nomsMale = getListFromCSV("./datos/hombres.csv")
    nomsFemale = getListFromCSV("./datos/mujeres.csv")
    surnames = getListFromCSV("./datos/apellidos-20.csv")
    poblaciones = getListFromCSV("./datos/poblacion.csv")

    db_main = DAL('sqlite://persons.db')
    crear_tablas(db_main)
    for x in range(elements):
        persona = Persona()
        persona.nif = getSpVatNumber()
        persona.sexo = getSexo()
        if persona.sexo == "M":
            persona.nombre = getValueListFromPosition(nomsMale, getRandomNumFromRange(len(nomsMale)))[0].capitalize()
        else:
            persona.nombre = getValueListFromPosition(nomsFemale, getRandomNumFromRange(len(nomsFemale)))[0].capitalize()
        persona.apellido1 = getValueListFromPosition(surnames, getRandomNumFromRange(len(surnames)))[0].capitalize()
        persona.apellido2 = getValueListFromPosition(surnames, getRandomNumFromRange(len(surnames)))[0].capitalize()
        posPoblacion = getRandomNumFromRange(len(poblaciones))
        persona.poblacion = getValueListFromPosition(poblaciones, posPoblacion)[0].capitalize()
        persona.provincia = getValueListFromPosition(poblaciones, posPoblacion)[1].capitalize()
        persona.email = getSpEmail(persona.nombre.lower(), persona.apellido1.lower(), persona.apellido2.lower())
        persona.movil = getSpMobileNumber()
        persona.f_nacimiento = getRandomDate()
        insertar_persona(db_main, persona)

p1 = Process(target=createpersons(1000000))
p2 = Process(target=createpersons(1000000))
p3 = Process(target=createpersons(1000000))
p4 = Process(target=createpersons(1000000))
p1.start()
p2.start()
p3.start()
p4.start()
p1.join()
p2.join()
p3.join()
p4.join()

