"""
create phone number and email extractor using regex
todo:
*1. search all phone numbers
*2. search all email addresses
3. return error if no numbers and emails
4. sort the numbers and emails in a not ugly way
5. copy them to the clipboard
"""

import re


searchText = '''Contact Us
Reach Us by Email - email is the best way to reach us

    Help with your order: support@nostarch.com
    Academic requests: academic@nostarch.com (Further information)
    Bulk and special sales questions: sales@nostarch.com
    Conference and event inquiries: conferences@nostarch.com
    Errata - please send any errata reports to: errata@nostarch.com
    General inquiries: info@nostarch.com
    Media requests: media@nostarch.com
    Proposals or editorial inquiries: editors@nostarch.com
    Rights inquiries: rights@nostarch.com

Reach Us by Mail

Our Mailing Address

No Starch Press
329 Primrose Road,  #42
Burlingame, CA 94010-4093
USA

Our Physical Address

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103
USA

NOTE: Below are our business phone numbers but we are a completely remote company. Please email support@nostarch.com with your questions and we will do our best to promptly resolve any issues that you may have.

Phone: 800.420.7240 or +1 415.863.9900
Fax: +1 415.863.9950
Reach Us on Social Media

Twitter Facebook Instagram Linkedin Pinterest'''

phoneNumberRegex = re.compile(r'''(
            (\d{3})               #area code
            (-|.)                 #seperator
            (\d{3})               #first 3 digits
            (-|.)                 #seperator
            (\d{3})               #last 4 digits
                                    )''', re.VERBOSE)


emailRegex = re.compile(r'''(
            [a-zA-Z0-9.+_]+
            @
            [a-zA-Z0-9.]+
            \.
            [a-zA-Z]{2,4}
                            )''', re.VERBOSE)

numbers = phoneNumberRegex.findall(searchText)
emails = emailRegex.findall(searchText)

print (numbers)
print (emails)