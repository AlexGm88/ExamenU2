'''
Tema: Examen Unidad 2
Fecha: 03 de octubre del 2022
Autor: Alejandro Galvez Maravilla
'''

def estudiantes():
    archivo = open('Estudiantes (1).prn', 'r')

    cadena = archivo.read()
    listEst = cadena.split("\n")

    archivo.close()
    list = set()
    for mnp in listEst:
        tupla=(mnp[:8], mnp[8:])
        list.add(tupla)
    return list

def materias():
    archivo = open('Kardex (1).txt', 'r')

    cadena = archivo.read()
    listEst = cadena.split("\n")

    archivo.close()
    conjunto = set()
    for mnp in listEst:
        mnp1 = mnp.split("|")
        tupla=(mnp1[0], mnp1[1], mnp1[2])
        conjunto.add(tupla)
    return conjunto

def info_estudiantes(*args):
    try:
        estudiante = estudiantes()
        materia = materias()
    except Exception as error:
        print("ERROR: ", error)
    list = []
    ban = True
    for info in args:
        for est in estudiante:
            dir = {}
            if info == int(est[0]):
                ban = False
                dir["Nombre"] = est[1]
                listaMaterias = []
                for mat in materia:
                    if info == int(mat[0]):
                        listaMaterias.append(mat[1])
                dir["Materias"] = listaMaterias
                list.append(dir)
    if ban:
        for est in estudiante:
            dir = {}
            dir["Nombre"] = est[1]
            listaMaterias = []
            for mat in materia:
                if int(est[0]) == int(mat[0]):
                    listaMaterias.append(mat[1])
            dir["Materias"] = listaMaterias
            list.append(dir)
    return list

try:
    datos=info_estudiantes()
except Exception as error:
    print("ERROR: ", error)
else:
    print(datos)

