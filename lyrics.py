import requests
import bs4
import os
import string

def main(text):
	for root, dirs, files in os.walk("."):
	    path = root.split('../bands')
	    for file in filter(lambda file: file.endswith('.txt'), files):
        	readF(open(os.path.join(root, file)).read())

def readF(archivo):
	print archivo
	#soup = bs4.BeautifulSoup(archivo)

	'''for a in soup.find_all('a', href=True):
		link = a['href']

		if not 'plyrics' in link:
			if not 'media.fastclick' in link:
				 if not 'azlyrics' in link:
				 	if not 'oldielyrics' in link:
						if not 'google' in link:
							if not 'azvideos' in link:
								getAlbums(link)'''