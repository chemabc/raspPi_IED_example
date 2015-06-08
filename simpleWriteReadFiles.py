# -*- coding: utf-8 -*-
#Trabajar con un archivo de texto

import codecs

textoAGrabar = "Hola, ¿cómo estás?"
nombreArchivoTexto = "exampleTextFile.txt"

#Imprime texto a escribir
print("Texto a Escribir")
print(textoAGrabar)

#ABRIR - ESCRIBIR - CERRAR
#Abrimos archivo
archivoTextoEscribir = open(nombreArchivoTexto, 'w')
#Le decimos que escriba nuestro mensaje:
archivoTextoEscribir.write(textoAGrabar)
#Cerramos el archivo
archivoTextoEscribir.close()

#ABRIR - LEER - CERRAR
#Abrimos archivo
archivoTextoLeer = open(nombreArchivoTexto, 'r')
#Le decimos que escriba nuestro mensaje:
contenidoArchivo = archivoTextoLeer.read()
#Cerramos el archivo
archivoTextoLeer.close()


#Imprime texto a escribir
print("Texto leído:")
print(contenidoArchivo)
