import os
sw = True
list_nombre = []
list_id = []
list_correo = []
list_contacto = []
list_edad = []
list_a_experiencia = []
list_profesion = []
list_ciudad = []
list_sexo = []

def fnt_limpiar():
    os.system('cls')
    print('Autor: Michell Mosquera')
    print('Fecha: 18 de abril del 2024\n\n')


def fnt_registrar(nombre, id , correo, contacto, edad, a_experiencia, profesion, ciudad, sexo):
    if nombre == '' or id == '' or correo == '' or contacto or edad == '' or a_experiencia == '' or profesion == '' or ciudad == '' or sexo == '':
        enter = input('\nError, debe de llenar todos los datos <ENTER>')
    else: 
        list_nombre.append(nombre)
        list_id.append(id)
        list_correo.append(correo)
        list_contacto.append(contacto)
        list_edad.append(edad)
        list_a_experiencia(a_experiencia)
        list_profesion.append(profesion)
        list_ciudad.append(ciudad)
        list_sexo.append(sexo)
        enter = input('\nRegistro exitoso <ENTER>')
                        
def fnt_selector(op):
    if op == '1':
        fnt_limpiar()
        id = input('Ingrese su ID: ')
        if id in list_id:
            enter = input('\nEsta persona ya se encuentra registrada <ENTER PARA CONTINUAR>')
        else:
            nombre = input('Nombre completo: ')
            correo = input('Correo: ')
            contacto = input('Contacto: ')
            edad = input('Edad: ')
            a_experiencia = input('Años de experiencia: ')
            profesion = input('Profesión \n1.Ing Sistema\n2. Ing Informatico\n-> ')
            ciudad = input('Ciudad: ')
            sexo = input('Sexo(M/F): ')
            if a_experiencia >= 2 and a_experiencia <= 4:
                fnt_registrar(nombre, id , correo, contacto, edad, a_experiencia, profesion, ciudad, sexo)    
            else:
                enter = input('\nNo cuentas con los años de experiencia necesarios para ser candidato<ENTER>')
            
    if op == '2':
        fnt_limpiar()
        for i in range(len(list_id)):
            print(f'{list_id[i]} {list_nombre[i]} {list_correo[i]} {list_contacto[i]} {list_edad[i]} {list_a_experiencia[i]} {list_profesion[i]}  {list_ciudad[i]}  {list_sexo[i]} ')
        enter = input('\Presione <ENTER> para continuar')
        
    if op == '3':
        sw = False


while sw == True:
    fnt_limpiar()
    opcion = input('\n\n ----- MENÚ PRINCIPAL -----\n1. Regristar\n2.Consultar\n3.Salir\n.-> ')
    fnt_selector(opcion)