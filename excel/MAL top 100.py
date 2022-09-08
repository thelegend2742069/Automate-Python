import requests, os, bs4, openpyxl


#request top 1-50 page
req1 = requests.get('https://myanimelist.net/topanime.php?')
page1 = bs4.BeautifulSoup(req1.text, 'html.parser')
#request top 51-100 page
req2 = requests.get('https://myanimelist.net/topanime.php?limit=50')
page2 = bs4.BeautifulSoup(req2.text, 'html.parser')

#open workbook and add titles in new worksheet
wb = openpyxl.Workbook()
ws = wb.active

ws['A1'] = 'Rank'
ws['B1'] = 'Anime'
ws['C1'] = 'Rating'


for i in range (50):
    #create list of anime and their ratings
    anime = page1.select('h3')[i].text
    rating = page1.select('span.text.on.score-label')[i]

    #write anime and their ratings to worksheet
    print('writing index %s...' % (str(i+1)))
    ws.cell(row=i+2, column=1, value=i+1)
    ws.cell(row=i+2, column=2, value=anime)
    ws.cell(row=i+2, column=3, value=rating.text)


for i in range (50):
    #create list of anime and their ratings
    anime = page2.select('h3')[i].text
    rating = page1.select('span.text.on.score-label')[i]
    
    #write anime and their ratings to worksheet
    print('writing index %s...' % (str(i+51)))
    ws.cell(row=i+52, column=1, value=i+51)
    ws.cell(row=i+52, column=2, value=anime)
    ws.cell(row=i+52, column=3, value=rating.text)


wb.save('MAL top 100.xlsx')