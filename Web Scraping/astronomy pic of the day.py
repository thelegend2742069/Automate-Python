import requests, os, bs4, re, datetime
from PIL import Image

def main(var):

    res = requests.get('https://apod.nasa.gov/apod/ap%s.html' %(var))       #get html page
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    image = soup.select('img')                          #get image css

    try:                                                #get image url
        imgURL = 'https://apod.nasa.gov/apod/'+image[0].get('src')
    except IndexError:                                  #return error if no image on requested day
        print('This day did not have an astropic.\nPlease check https://apod.nasa.gov/apod/ap%s.html' %(var))
        return
    
    imgres = requests.get(imgURL)                       #request image page
    imgres.raise_for_status
    
    print('downloading image...\n\n')
    imgFile = open('Astronomy Pic of the Day/AstroPic %s.jpg' %(var), 'wb')
    for chunk in imgres.iter_content(100000):           #download picture in chunks of 100kb
        imgFile.write(chunk)
    imgFile.close()
    
    
    imgopen = Image.open('Astronomy Pic of the Day/AstroPic %s.jpg' %(var)) #open image in image viewer
    imgopen.show()


    explan = re.sub(r'(\s+|\n)', ' ', soup.select('p')[2].text).strip()     #print explanation of image
    print('\n\n'+explan.split(' Tomorrow')[0])

os.makedirs('Astronomy Pic of the Day', exist_ok=True)                              #make directory for pictures, skip if already exists
date = input("Enter a date (after 1995 June 20) in YYMMDD format ('today' and 'yesterday' are also fine): ")

if date == 'today':                                                         #check for relative dates
    date = re.sub('-','', str(datetime.date.today())[2:])

elif date == 'yesterday':
    date = re.sub('-','', str(datetime.date.today())[2:])
    date = str(int(date)-1)
elif len(date) != 6:
    print('This is not a valid date.')
    exit()
main(date)