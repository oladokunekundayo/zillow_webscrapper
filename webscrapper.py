#this code is for personal use only and is not authorized for distribution
from bs4 import BeautifulSoup as soup
import urllib.request

#puts all the sites into a list so i can perform a loop on it
site=['https://www.zillow.com/homedetails/6891-E-Cody-Ct-Camby-IN-46113/305260104_zpid/'
,'https://www.zillow.com/homedetails/0-Salt-Creek-Rd-Nashville-IN-47448/2104621747_zpid/'
,'https://www.zillow.com/homedetails/14-Dynasty-Ridge-Rd-Martinsville-IN-46151/2078243979_zpid/'
,'https://www.zillow.com/homedetails/W-Deer-Ridge-Trl-Martinsville-IN-46151/217901010_zpid/'
,'https://www.zillow.com/homedetails/00-Salt-Creek-Rd-Nashville-IN-47448/2098892429_zpid/'
,'https://www.zillow.com/homedetails/0-E-Shore-Dr-Morgantown-IN-46160/2078769728_zpid/'
,'https://www.zillow.com/homedetails/E-County-Road-925-S-Marengo-IN-47140/102884213_zpid/'
,'https://www.zillow.com/homedetails/1601-Rodenberg-Ct-Evansville-IN-47720/200461109_zpid/'
,'https://www.zillow.com/homedetails/N-Side-E-Saylor-Rd-Salem-IN-47167/245160795_zpid/'
,'https://www.zillow.com/homedetails/3255-E-Lemon-Rd-Canaan-IN-47224/2076773984_zpid/'
,'https://www.zillow.com/homedetails/3716-N-Kindred-Rdg-Martinsville-IN-46151/217898445_zpid/']

#I dont think you have to pre-define this in python like you do in java but i did anyway
count = 0

#Just put the entire script into a loop
#python is cool because you can define a varible as you use is for example, i am defining web as i use it in this loop
for web in site:
	req = urllib.request.Request(
    		web,
    		data=None, 
    		headers={
        	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
    		}
	)

	#opens connection with the url
	f = urllib.request.urlopen(req)
	#reads the web page as an html page
	page_soup = soup(f.read(), "html.parser")
	#closes the connction
	f.close()

	#defines each part i want grab by searching for a specific tag
	address = page_soup.find("h1").get_text()
	price = page_soup.find("h4")
	acres = page_soup.find("span", {"class":"ds-bed-bath-living-area"})
	status = page_soup.find("span", {"class":"sc-qZtCU kNVxeh ds-status-details"}).get_text()
	#removes the tags by replacing them with empty string
	#for price
	for span in price:
		price = span.text.replace('<span>', '').strip()
	#for acres
	for span in acres:
		acres = span.text.replace('<span>', '').strip()
	count+=1
	print("(",count,")", address)
	print(acres,',',price,',',status)
	


#Make sure you SMASH that LIKE button! Like comment and subscribe!
