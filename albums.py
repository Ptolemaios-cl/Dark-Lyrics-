#ciclo con las letras del alfabeto para traer nombres de artistas desde dark lyrics
import requests
import bs4
import os
import string


def getAlbums(text):
	# traverse root directory, and list directories as dirs and files as files
	for root, dirs, files in os.walk("."):
	    path = root.split('/')
	    print (len(path) - 1) *'---' , os.path.basename(root)       
	    for file in files:
	        print len(path)*'---', file

getAlbums("lol")