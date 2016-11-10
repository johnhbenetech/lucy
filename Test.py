from urllib.request import urlopen
from bs4 import BeautifulSoup

dogs = []
breeds = []
lucys = []

html = urlopen("https://www.sfspca.org/adoptions/dogs")
soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a'):
	if "pet-details" in str(link.get('href')):
		dogs.append("https://www.sfspca.org"+str(link.get('href')))
		
dogs=list(set(dogs))
		
for dog in dogs:
	html = urlopen(dog)
	soup = BeautifulSoup(html, 'html.parser')
	breeds.append([dog,str(soup.find("div", { "class" : "field-name-field-possible-primary-breed" }).find("div",{"class" : "field-item even"}).text).strip()])

for breed in breeds:
	if "Boston" in breed[1]:
		print(breed[0])