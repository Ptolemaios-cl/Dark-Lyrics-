import requests
import bs4
import os
import string
from collections import OrderedDict
import time

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

def main(text):
	for root, dirs, files in os.walk("bands"):
	    path = root.split('/bands')
	    for file in filter(lambda file: file.endswith('.txt'), files):
        	readF(open(os.path.join(root, file)).read())

def readF(archivo):
		archivo = archivo.replace(' " ', "")
		archivo = archivo.replace("[", "")
		archivo = archivo.replace("#", "")
		archivo = archivo.replace("]", "")
		archivo = archivo.replace(" ", "")
		archivo = archivo.replace("u'", "'")
		archivo = archivo.strip()
		archivo = archivo.split(",")
		lista = remove_duplicates(archivo)
		for link in lista:
			if link.strip() != "":
				thelink = link.strip().replace("'", "")
				band = (link.split("/")[1])
				album = str(link.split("/")[2]).replace(".html", "")
				album = str(album.replace("'", ""))
				print thelink, band, album
				getLyric(thelink, band, album)

def getLyric(link, band_name, album):
	response = requests.get('http://www.darklyrics.com/'+link)
	response.encoding = "utf-8"
	soup = bs4.BeautifulSoup(response.text)

	band = soup.select('h1');                 #select the album class
	album_info = soup.select('div.albumlyrics');                 #select the album class
	lyrics = soup.select('div.lyrics');                 #select the lyrics class

	lyrics_string = str(lyrics[0]) #convert to a string
	albums = str(album_info[0]) #convert to a string

	ruta = "/-^JobZ^-/Dark Lyrics/lyrics" #ruta carpeta para guardar txt
	carpeta = os.path.abspath(ruta+"/"+band_name)
	if not os.path.exists(carpeta):
		os.makedirs(carpeta)
	completeName = carpeta + "/%s.txt" % album
	file1 = open(completeName, "w")
	file1.write("%s \n %s \n %s \n" % (band, albums, lyrics_string))	
	file1.close()	
	print band_name+","+album+"|---> Ok (30 segundos)"
	time.sleep(30)

main("lol")
#getLyric('lyrics/agoraphobicnosebleed/splitwithgob.html', 'agoraphobicnosebleed', 'splitwithgob') #test con 1 album. ok
