"""
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase charac-
ters, and has at least one digit. You may need to test the string against mul-
tiple regex patterns to validate its strength.
"""

import re

smallCheck = re.compile('[a-z]+')       #check for small letters
capitalCheck = re.compile('[A-Z]+')     #check for capital letters
numCheck = re.compile('[0-9]+')         #check for numbers


def main(given):
    match = []
    if len(given)<8:                    #check if password length atleast 8
        print('\nPassword is weak.\n')
    else:
        match.append(smallCheck.findall(given))
        match.append(capitalCheck.findall(given))
        match.append(numCheck.findall(given))
        for i in match:
            if len(i)==0:               #check if any of the 3 conditions is not met
                print('\nPassword is weak.\n')
                match = []              #set match as empty list so it does not say-
                break                   #password is strong with unmet conditions
        if match != []: print('\nPassword is strong.\n')



password = input('Enter a password. I will check if it is strong or not.\n')


main(password)

while True:
    password = input('Enter another password to check. Leave blank to exit.\n')
    if password == '':
        break                   #exit program if nothing is input
    else:
        main(password)