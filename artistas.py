#ciclo con las letras del alfabeto para traer nombres de artistas desde dark lyrics
import requests
import bs4
import os
import string


allTheLetters = string.ascii_lowercase
ruta = "/-^JobZ^-/Dark Lyrics" #ruta carpeta para guardar txt

def getArtists(text):
  lowerText = text.lower()
  for letter in allTheLetters:
	response = requests.get('http://www.darklyrics.com/'+letter+'.html')
	response.encoding = "utf-8"

	carpeta = os.path.abspath(ruta+"/%s" % letter)
	if not os.path.exists(carpeta):
		os.makedirs(carpeta)

	soup = bs4.BeautifulSoup(response.text)
	lyrics_l = soup.find_all("div", class_="fl")
	lyrics_r = soup.find_all("div", class_="fr")
	[br.extract() for br in lyrics_l[0].findAll('<br>')] #no se si sirve aun pero la idea es que si
	[br.extract() for br in lyrics_l[0].findAll('<br/>')] #no se si sirve aun pero la idea es que si
	#print(str(lyrics_l))
	#print(str(lyrics_r))
	completeName = carpeta + "/%s.txt" % letter
	file1 = open(completeName, "w")
	toFile = str(lyrics_l) + str(lyrics_r)

	file1.write(toFile)
	file1.close()

getArtists("lol")