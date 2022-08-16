"""
How would you write a regex that matches a sentence where the first
word is either Alice, Bob, or Carol; the second word is either eats, pets, or
throws; the third word is apples, cats, or baseballs; and the sentence ends
with a period? This regex should be case-insensitive. It must match the
following:
• 'Alice eats apples.'
• 'Bob pets cats.'
• 'Carol throws baseballs.'
• 'Alice throws Apples.'
• 'BOB EATS CATS.'
but not the following:
• 'RoboCop eats apples.'
• 'ALICE THROWS FOOTBALLS.'
• 'Carol eats 7 cats.'
"""

import re

checker = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)

sentence = input('Enter a sentence\n')
while len(sentence)>0:
    match = checker.findall(sentence)
    if match == []:
        print('The entered sentence does not match.')
    else:
        print('This entered sentence matches:\n'+str(match))
    sentence = input('\nEnter another sentence. Leave it blank to exit\n')
print('Goodbye.')