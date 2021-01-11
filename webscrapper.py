import urllib.request
req = urllib.request.Request(
    'https://www.zillow.com/homedetails/3255-E-Lemon-Rd-Canaan-IN-47224/2076773984_zpid/', 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
    }
)

f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))