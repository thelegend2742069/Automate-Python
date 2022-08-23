import requests, os, bs4, openpyxl

req1 = requests.get('https://myanimelist.net/topanime.php?')
page1 = bs4.BeautifulSoup(req1.text, 'html.parser')

req2 = requests.get('https://myanimelist.net/topanime.php?limit=50')
page2 = bs4.BeautifulSoup(req2.text, 'html.parser')


wb = openpyxl.Workbook()
ws = wb.active

ws['A1'] = 'Rank'
ws['B1'] = 'Anime'
ws['C1'] = 'Rating'


for i in range (50):
    anime = page1.select('h3')[i].text
    rating = page1.select('span.text.on.score-label')[i]

    print('writing index %s...' % (str(i+1)))
    ws.cell(row=i+2, column=1, value=i+1)
    ws.cell(row=i+2, column=2, value=anime)
    ws.cell(row=i+2, column=3, value=rating.text)


for i in range (50):
    anime = page2.select('h3')[i].text
    rating = page1.select('span.text.on.score-label')[i]
    
    print('writing index %s...' % (str(i+51)))
    ws.cell(row=i+52, column=1, value=i+51)
    ws.cell(row=i+52, column=2, value=anime)
    ws.cell(row=i+52, column=3, value=rating.text)

    
wb.save('MAL top 100.xlsx')