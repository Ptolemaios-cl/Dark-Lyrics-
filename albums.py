#ciclo con las letras del alfabeto para traer nombres de artistas desde dark lyrics
import requests
import bs4
import os
import string


def main(text):
	for root, dirs, files in os.walk("."):
	    path = root.split('/')
	    for file in filter(lambda file: file.endswith('.txt'), files):
        	getBand(open(os.path.join(root, file)).read())

def getBand(archivo):	
	soup = bs4.BeautifulSoup(archivo)

	for a in soup.find_all('a', href=True):
		link = a['href']

		if not 'plyrics' in link:
			if not 'media.fastclick' in link:
				 if not 'azlyrics' in link:
				 	if not 'oldielyrics' in link:
						if not 'google' in link:
							if not 'azvideos' in link:
								print link

def getAlbums(link):	
	response = requests.get('http://www.darklyrics.com/'+link)
	response.encoding = "utf-8"
	soup = bs4.BeautifulSoup(response.text)	
	for a in soup.find_all('a', href=True):
		album_link = a['href']
		band_name = link.replace(".html", "")				
		band_name = band_name[2:]
		if band_name in album_link:
			if '#1' in album_link:
				print album_link[3:-2]

#main("lol")
getAlbums("a/aaaarrghh.html")