import requests, os, bs4, re
from PIL import Image

def main(var):
    res = requests.get('https://apod.nasa.gov/apod/ap%s.html' %(var))
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    image = soup.select('img')

    
    imgURL = 'https://apod.nasa.gov/apod/'+image[0].get('src')
    imgres = requests.get(imgURL)
    imgres.raise_for_status
    

    imgFile = open('Astronomy Pic of the Day/AstroPic %s.jpg' %(var), 'wb')
    for chunk in imgres.iter_content(100000):
        imgFile.write(chunk)
    imgFile.close()
    
    
    imgopn = Image.open('Astronomy Pic of the Day/AstroPic %s.jpg' %(var))
    imgopn.show()


    explan = re.sub(r'(\s+|\n)', ' ', soup.select('p')[2].text).strip()
    print('\n\n'+explan.split(' Tomorrow')[0])

os.makedirs('Astronomy Pic of the Day', exist_ok=True)
date = input("Enter a date in YYMMDD format (after 1995 June 20): ")
main(date)

