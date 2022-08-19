import requests, os, bs4, re, random
from PIL import Image


def xkcd_comic(number):
    res2 = requests.get("https://xkcd.com/%s/" % (str(number)))
    soup = bs4.BeautifulSoup(res2.text, 'html.parser')

    title = str(soup.select('#ctitle'))
    elem = soup.select('#comic img')
    

    comicUrl = 'https:'+elem[0].get('src')
    res3 = requests.get(comicUrl)

    image = open("xkcd/xkcd #%s: %s.jpg" % (str(number), title[18:-7]), 'wb')
    print("\nDownloading...")

    for chunk in res3.iter_content(100000):
        image.write(chunk)
    image.close()

    print("\nShowing Comic #"+str(number)+': '+title[18:-7])
    im = Image.open("xkcd/xkcd #%s: %s.jpg" % (str(number), title[18:-7]))
    im.show()


    

res = requests.get("https://xkcd.com")
res.raise_for_status()


current_finder = re.compile(r'/(\d+)/')
current = current_finder.findall(res.text)[0]


os.makedirs('xkcd', exist_ok=True)


issue = input('Enter an xkcd issue from 1 to '+current+' (or leave it blank for a random issue):\n')

if not issue:
    issue = random.randint(1, int(current))
    xkcd_comic(issue)
else:
    xkcd_comic(int(issue))