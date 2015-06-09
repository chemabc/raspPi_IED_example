# -*- coding: utf-8 -*-
#importamos la libreria tweepy para acceder de forma sencilla
#a la API de Twitter
import tweepy
import os
import codecs
 
#Aqui van nuestras claves de acceso a Twitter, obtenidas en http://dev.twitter.com
CONSUMER_KEY = '' 
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
 
#Primero nos identificamos ante Twitter con nuestras claves
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#guardamos en la variable "twitter" el objeto que nos da acceso a Twitter
twitter = tweepy.API(auth)


#definimos función para recoger más de un tweet y guardarlo en una lista
archivo = "tweetsRecogidos.txt"
def buscaTweets(listaPalabras, numTweets):
    #abrimos archio de texto para escritura (write)
    archivoTexto = open(archivo, 'w')
    for tweets in twitter.search(q=listaPalabras,count=numTweets, result_type='recent'):
        #para cada tweet sacamos por pantalla la fecha de creacion
        print(tweets.created_at)
        #el nombre de usuario
        print(tweets.user.screen_name)
        # y el texto
        tweetText = str(tweets.text.encode('utf-8'))
        print("TWEET TEXT: \n" + tweetText)
        #Codificar con UTF-8 (para que funcionen las tildes) y
        # grabar a archivo de texto
        archivoTexto.write(tweetText)
        # despues ponemos 40 asteriscos como separador con el proximo tweet
        print(' *'*40)
    #Cerramos archivo
    archivoTexto.close()
    return True



lTweets = buscaTweets(['Maduro'], 2)


def robotFile(filetext):
    os.system("espeak -ves -f '" + filetext + "' --stdout | aplay" )


robotFile(archivo)
