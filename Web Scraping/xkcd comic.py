import requests, os, bs4, re, random
from PIL import Image


def xkcd_comic(number):
    res2 = requests.get("https://xkcd.com/%s/" % (str(number)))     #get requested comic issue html page
    soup = bs4.BeautifulSoup(res2.text, 'html.parser')

    title = str(soup.select('#ctitle'))             #get title html code
    elem = soup.select('#comic img')                #get image html code

    comicUrl = 'https:'+elem[0].get('src')          #get image url
    res3 = requests.get(comicUrl)

    image = open("xkcd/xkcd #%s: %s.jpg" % (str(number), title[18:-7]), 'wb')
    print("\nDownloading...")

    for chunk in res3.iter_content(100000):         #download image in chunks of 100kb
        image.write(chunk)
    image.close()

    print("\nShowing Comic #"+str(number)+': '+title[18:-7])
    im = Image.open("xkcd/xkcd #%s: %s.jpg" % (str(number), title[18:-7]))      #open image in image viewer
    im.show()


    

res = requests.get("https://xkcd.com")          #get xkcd html page
res.raise_for_status()


current_finder = re.compile(r'/(\d+)/')         #find latest issue number
current = current_finder.findall(res.text)[0]


os.makedirs('xkcd', exist_ok=True)              #make directory xkcd, skip if it already exists


issue = input('Enter an xkcd issue from 1 to '+current+' (or leave it blank for a random issue):\n')

if not issue:
    issue = random.randint(1, int(current))     #choose random issue number if no input (random function includes upper bound)
    xkcd_comic(issue)
else:
    xkcd_comic(int(issue))