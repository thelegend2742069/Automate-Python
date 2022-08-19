import re, pyperclip, os, bs4, requests

"""
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())


var1='apple'
var2='banana'
pyperclip.copy(var1+'\n\n'+var2)
pyperclip.paste()


name = input('What is your name?')
while name != '':
    print('Hello %s, lovely day today!', name)
    name=input('What is your name? Leave blank to exit.')
print('Goodbye.')
"""


"""
checker = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
match = checker.findall('''
                    Alice eats apples.
                    Bob pets cats.
                    Carol throws baseballs.
                    Alice throws Apples.
                    BOB EATS CATS.
                    RoboCop eats apples.
                    ALICE THROWS FOOTBALLS.
                    Carol eats 7 cats.
                    ''')

"""

"""
print(match)
sentence = input("\n")
match = checker.findall(sentence)
print(match)

for i in match:
    if len(i)==0:
        print('\nPassword is weak.')
        match = []
        break
"""


"""
os.makedirs('TestFiles')

for i in range(1,11):
    quizFile = open('TestFiles/Test File '+str(i)+'.txt', 'w')
    quizFile.write('test file number '+str(i))
    quizFile.close()
    quizFile = open('TestFiles/Test File '+str(i)+'.txt')
    print(quizFile.read()+'\n')
    quizFile.close()    
"""

res = requests.get("https://xkcd.com")
#print(res.text)
current_finder = re.compile(r'/(\d+)/')
print(current_finder.findall(res.text)[0])