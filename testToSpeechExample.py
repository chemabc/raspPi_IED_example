# -*- coding: utf-8 -*-

#Text to speech example
# Speech synthetizer: eSpeak

'''Para empezar hay que forzar a que se use la salida de Headphones de
Raspberry, o yendo a pyhtonGames y forzando headphones o
escribiendo: amixer cset numid=3 1
'''
#Importamos los módulos apropiados que tienen funciones que nos serán útiles luego
import os, time
import codecs

#El sistema leerá lo que haya en el archivo
nombreArchivo = "archivoALeer.txt"
'''
archivo = open(nombreArchivo, 'w')
archivo.write("hola que tal")
archivo.close()

archivo = open(nombreArchivo, 'r')
contenido = archivo.read()
archivo.close()
'''

#Para nuesto conversor de texto a voz, primero definimos una función
#que acepta una variable (texto = string = "bla bla" = 'bla bla') como parámetro:
def robotText(text):
    os.system("espeak -ves ' " + text + " '")
    
def robotFile(textFile):
    os.system("espeak -ves -f '" + textFile + "' --stdout | aplay")

print("Vamos a decir el contenido del archivo")
#robotText(contenido)
robotFile(nombreArchivo)

