import sys
sys.path.insert(0, '../model')
import datetime
from pydal import DAL, Field
import person

def crear_tablas(db):
    try:
        db.person.drop()
    except Exception:
        print('No data on the database')

    db.define_table('person',
                    Field('id', type='id'),
                    Field('nif'),
                    Field('sexo'),
                    Field('nombre'),
                    Field('apellido1'),
                    Field('apellido2'),
                    Field('f_nacimiento', type='date'),
                    Field('poblacion'),
                    Field('provincia'),
                    Field('movil'),
                    Field('email'),
                    )

def insertar_persona(db, persona):
    db.person.insert(nif=persona.nif,
                       sexo=persona.sexo,
                       nombre=persona.nombre,
                       apellido1=persona.apellido1,
                       apellido2=persona.apellido2,
                       f_nacimiento=persona.f_nacimiento,
                       poblacion=persona.poblacion,
                       provincia=persona.provincia,
                       movil=persona.movil,
                       email=persona.email)
    db.commit()

