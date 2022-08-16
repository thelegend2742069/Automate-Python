"""
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase charac-
ters, and has at least one digit. You may need to test the string against mul-
tiple regex patterns to validate its strength.
"""

import re

smallCheck = re.compile('[a-z]+')
capitalCheck = re.compile('[A-Z]+')
numCheck = re.compile('[0-9]+')


def main(given):
    match = []
    if len(given)<8:
        print('\nPassword is weak.')
    else:
        match.append(smallCheck.findall(given))
        match.append(capitalCheck.findall(given))
        match.append(numCheck.findall(given))
        for i in match:
            if len(i)==0:
                print('\nPassword is weak.')
                match = []
                break
        if match != []: print('\nPassword is strong.\n'+str(match))

password = input('Enter a password. I will check if it is strong or not.\n')


main(password)