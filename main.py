from modelos.persona import Person
from arbol import ArbolBinario
from letters_assign import search
from LZWCompresor import LZWCompression
import coding_decoding
import json
import csv


jsonArbol = ArbolBinario()
compression = LZWCompression()

menu = ""

while(menu != None):
    print("1. Cargar archivo\n")
    print("2. Buscar por nombre (rango)\n")
    print("3. Buscar por dpi (individual)\n")
    print("4. Eliminar por Nombre (rango)\n")
    print("5. Eliminar por dpi (individual)\n")
    print("6. Actualizar por Nombre (rango)\n")
    print("7. Actualizar por dpi (individual)\n")
    print("8. Codificar por dpi\n")
    print("9. Decodificar por dpi\n")
    print("10. Comprimir Cartas (individual)\n")
    print("11. Descomprimir Cartas (individual)\n")
    print("12. Salir")
    menu = input()

    if(menu == "1"):
        print("Cargando archivo...")
        with open('input.csv') as archivo:
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                jsonPersona = Person.from_json(str(fila[1]))
                jsonPersona.letter = search(jsonPersona)
                if fila[0] == "INSERT":
                    #ponerle sus cartas de recomendacion
                    jsonArbol.insertar(jsonPersona)
                    
                elif fila[0] == "PATCH":
                    
                    if ((jsonArbol.buscar(jsonPersona))!= None):
                        
                        jsonPersonaPatch = jsonArbol.buscar(jsonPersona)
                        jsonPersonaPatch.datebirth = jsonPersona.datebirth
                        jsonPersonaPatch.address = jsonPersona.address
                        jsonPersonaPatch.companies = jsonPersona.companies
                        jsonPersonaPatch.letter = jsonPersona.letter

                        jsonArbol.eliminar(jsonPersona)
                        jsonArbol.insertar(jsonPersonaPatch)
                    else:
                        print("No se encontro a la persona")
                elif fila[0] == "DELETE":
                    jsonArbol.eliminar(jsonPersona)
                else:
                    print("No es una instruccion valida")
        print("Se cargo el archivo correctamente")
    elif(menu == "2"):
        print("Buscar por nombre")
        print("Coloque el nombre de las personas que quiere buscar:")
        nombre = input()
        lista = jsonArbol.buscar_por_nombre(nombre.lower())
        i =0
        while i < len(lista):
            print("Nombre:" + lista[i].name)
            print("Dpi:" + lista[i].dpi)
            print("Fecha de nacimiento:" + lista[i].datebirth)
            print("Direccion:" + lista[i].address)
            print("Companias:" + str(lista[i].companies))
            print("Cartas:" + str(lista[i].letter))
            print("No. de Cartas:" + str(len(lista[i].letter)))
            print('\n')
            i += 1
        print("Se encontraron:" + str(i) +" resultados.")
    elif(menu == "3"):
        print("Buscar por dpi")
        print("Coloque el dpi de la persona que quiere buscar:")
        dpi = input()
        lista = jsonArbol.buscar_por_dpi(dpi)
        i =0
        while i < len(lista):
            print("Nombre:" + lista[i].name)
            
            print("Dpi:" + lista[i].dpi)
            print("Fecha de nacimiento:" + lista[i].datebirth)
            print("Direccion:" + lista[i].address)
            print("Companias:" + str(lista[i].companies))
            print('\n')
            print("Cartas:" + str(lista[i].letter))
            print('\n')
            print("No. de Cartas:" + str(len(lista[i].letter)))
            print('\n')
            i += 1
        print("Se encontraron:" + str(i) +" resultados.")
    elif(menu == "4"):
        print("Eliminar por Nombre")
        print("Coloque el nombre de las personas que quiere eliminar:")
        nombre = input()
        lista = jsonArbol.buscar_por_nombre(nombre.lower())
        i =0
        while i < len(lista):
            jsonArbol.eliminar(lista[i])
            i += 1
        print("Se eliminaron: " + str(i) +" personas.")

    elif(menu == "5"):
        print("Eliminar por dpi")
        print("Coloque el dpi de la personas que quiere eliminar:")
        nombre = input()
        lista = jsonArbol.buscar_por_dpi(nombre)
        i =0
        while i < len(lista):
            jsonArbol.eliminar(lista[i])
            i += 1
        print("Se eliminaron: " + str(i) +" personas.")
    elif(menu == "6"):
        print("Actualizar por nombre")
        print("Coloque el nombre de las personas que quiere actualizar:")
        nombre = input()
        lista = jsonArbol.buscar_por_nombre(nombre.lower())
        print("Coloque la Fecha de nacimiento (en caso de no querer cambiar dar ENTER):")
        fecha = input()
        print("Coloque la direccion (en caso de no querer cambiar dar ENTER):")
        direccion = input()
        if (fecha != '') & (direccion == ''):
            i =0
            while i < len(lista):
                lista[i].datebirth = fecha
                i += 1
        elif (fecha == '') & (direccion != ''):
            i =0
            while i < len(lista):
                lista[i].address = direccion
                i += 1
        elif (fecha != '') & (direccion != ''):
            i =0
            while i < len(lista):
                lista[i].datebirth = fecha
                lista[i].address = direccion
                i += 1
        else:
            print("No se hacen cambios")
    elif(menu == "7"):
        print("Actualizar por dpi")
        print("Coloque el dpi de la persona que quiere actualizar:")
        dpi = input()
        lista = jsonArbol.buscar_por_dpi(dpi)
        print("Coloque la Fecha de nacimiento (en caso de no querer cambiar dar ENTER):")
        fecha = input()
        print("Coloque la direccion (en caso de no querer cambiar dar ENTER):")
        direccion = input()
        if (fecha != '') & (direccion == ''):
            i =0
            while i < len(lista):
                lista[i].datebirth = fecha
                i += 1
        elif (fecha == '') & (direccion != ''):
            i =0
            while i < len(lista):
                lista[i].address = direccion
                i += 1
        elif (fecha != '') & (direccion != ''):
            i =0
            while i < len(lista):
                lista[i].datebirth = fecha
                lista[i].address = direccion
                i += 1
        else:
            print("No se hacen cambios")
    elif(menu == "8"):
        print("Codificando el atributo \"dpi\" de los objetos \"persona\"...")
        dpi = input("Ingrese el dpi el cual quiere codificar... \n")
        lista_persona = jsonArbol.buscar_por_dpi(dpi)
        if lista_persona != []:
            persona = lista_persona[0]
            persona_dpi_codificado = coding_decoding.codificar(dpi, persona.companies)
            print(f"Codificacion exitosa! , el numero de dpi codificado es: {persona_dpi_codificado}")
        else:
            print("No se encuentra a la persona del dpi que ingreso intente de nuevo...")
    elif(menu == "9"):
        print("Decodificacion por dpi encodeing")
        dpiencodeing = input("Ingrese el dpi codificado de la persona que quiere decodificar \n")
        dpi = str(coding_decoding.decodificar(dpiencodeing))
        lista_persona = jsonArbol.buscar_por_dpi(dpi)
        if lista_persona != []:
            print("Decodificacion existosa!")
            print("Nombre:" + lista_persona[0].name)
            print("Dpi:" + lista_persona[0].dpi)
            print("Fecha de nacimiento:" + lista_persona[0].datebirth)
            print("Direccion:" + lista_persona[0].address)
            print("Companias:" + str(lista_persona[0].companies))
            print("Cartas:" + str(lista[i].letter))
            print("No. de Cartas:" + str(len(lista[i].letter)))
            print('\n')
        else:
            print("No se pudo decodificar...")
            
    elif(menu == "10"):
        dpi = input("Ingrese el dpi del cual quiere comprimir las cartas \n")
        lista = jsonArbol.buscar_por_dpi(dpi)
        i = 0
        while i < len(lista[0].letter):
            lista[0].letter[i] = compression.compress(lista[0].letter[i])
            i += 1
        print("Se han comprimido las cartas!")
        
    elif(menu == "11"):
        dpi = input("Ingrese el dpi del cual quiere descomprimir las cartas \n")
        lista = jsonArbol.buscar_por_dpi(dpi)
        i = 0
        while i < len(lista[0].letter):
            lista[0].letter[i] = compression.decompress(lista[0].letter[i])
            i += 1
        print("Se han descomprimido las cartas!")
        
    elif(menu == "12"):
        menu = None