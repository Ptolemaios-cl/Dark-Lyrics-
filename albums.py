#ciclo con las letras del alfabeto para traer nombres de artistas desde dark lyrics
import requests
import bs4
import os
import string


def getAlbums(text):	
	for root, dirs, files in os.walk("."):
	    path = root.split('/')	    
	    for file in filter(lambda file: file.endswith('.txt'), files):
	        print len(path)*'---', file

getAlbums("lol")