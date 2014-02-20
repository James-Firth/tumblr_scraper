from bs4 import BeautifulSoup
import urllib, sys, getopt, unicodedata

for x in {"","page/2","page/3","page/4","page/5"}:
	print "Scraping page "+x
	f = urllib.urlopen('http://posterology.tumblr.com/tagged/Breaking+Bad/chrono/'+x).read()
	soup = BeautifulSoup(f)
	for link in soup.find_all('img'):
		if isinstance(link.get('alt'), unicode):
			fname = link.get('alt')
			fname =  fname[:(fname.find('\n'))]
			ref = link.get('src')
			ext = ref[-3:]
			if ext == "jpg":
				fname = fname.replace("/", "-")
				fname = (fname +"."+ ext)
				fname = unicodedata.normalize("NFKD", fname).encode('ascii', 'ignore')
				print(ref,fname)
				urllib.urlretrieve(ref, fname)
