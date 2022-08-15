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


searchText1 = input('Input the text to search phone numbers and email addresses in. Leave it blank to search default text.\n')


if searchText1 == '':
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


searchText2 ='''
            
Choose another country or region to see content specific to your location.
Continue
Contacting Apple
Sales and Product Inquiries
Apple Online Store

Apple.com is a convenient place to purchase Apple products and accessories from Apple and other manufacturers. You can buy online or call (800) MY–APPLE (800–692–7753).

You can get information about an order you placed on the Apple Online Store through the Order Status page. If you prefer, you can also get order status or make changes by phone at (800) 692–7753.
Shop with SignTime ASL Support

American Sign Language (ASL) interpreters are available for all your online shopping needs, right in your web browser. Connect to an interpreter
Apple Retail Stores

Experience the digital lifestyle at any of the Apple Retail Stores around the country. Find store hours and contact information for all locations.
Get Financing for You, Your Business, or Your School

Apple Financial Services offers financing on Apple products for consumers, educational institutions, and businesses. Speak with your Apple representative to learn more.
Find Consultants

Visit our Apple Consultants Network page to find a consultant in the U.S. or Canada.
Find Authorized Training Providers

Visit the Apple Training website for information on available courses and Apple Authorized Training Providers worldwide.
How to Buy for Business

If you are a business or professional user, visit the Apple Store for Business or call 1–800–854–3680.

Corporate and Government Sales:

    Apple Enterprise Sales (877) 412–7753
    Apple Government Sales (877) 418–2573

How to Buy for Education

If you are a student or teacher, visit the Apple Store for Education or call 1–800–692–7753.

If you are buying on behalf of an educational institution, visit the Apple Store for Education Institutions or call 1–800–800–2775, 7 days a week from 9 AM to 6 PM central time7 days a week from 9:00 a.m. to 6:00 p.m. Central time.
Find Apple Authorized Resellers

Use our Reseller Locator to find an Apple Authorized Reseller in the U.S.

Apple Authorized Resellers offer industry expertise, multi-platform services, and Mac-based solutions for a wide variety of organizations.
North American Corporate Contacts

United States

    Apple Media Helpline (408) 974–2042
    Apple Software Upgrade Center (888) 840–8433
    Reseller Referral (Resellers, Trainers, Consultants) (800) 538–9696

Canada

    Apple Store (Consumer and Education Individuals) (800) MY–APPLE (800–692–7753)

Mexico

    Apple Store (Consumer and Education Individuals) 001–800–MY–APPLE (001–800–692–7753)
    Apple Store (Small Business) 001–800–692–7753

Product and Services Support
Contact Apple Support

Need service or support? Start your request online and we’ll find you a solution.

More Ways to Get Help:

    U.S. technical support: (800) APL–CARE (800–275–2273)
    See all worldwide support telephone numbers
    Contact a mobile carrier
    Make a reservation at an Apple Retail Store Genius Bar
    Beats support:
    (800) 442–4000 (U.S.) or see all worldwide support telephone numbers

Get ASL Support through SignTime

You can also receive AppleCare service and support in American Sign Language (ASL). Connect to an interpreter

If you are a customer with a disability and utilize our accessibility features such as VoiceOver or MFi Hearing devices, call (877) 204–3930 for direct access to Apple representatives who are trained in providing support for these services.

Most Apple products are eligible for 90 days of complimentary technical support. Online technical support for Apple products is available beyond the initial 90 days.
Browse Online Support

Visit the Apple Support site for quick answers, manuals, and in-depth technical articles. Visit Apple Support Communities to get help and tips from fellow Apple customers.

For help with Beats by Dre headphones and speakers, visit Beats Support. For help with the Beats Music streaming service, visit Beats Music Support.
Lost or Stolen Apple Products

If you have lost or found an Apple product, contact your local law-enforcement agency to report it. You can also find a list of serial numbers associated with your Apple ID and get information about using Find My iPhone for iPhone, iPad, iPod touch, or Mac.
Legal

For legal questions, please go to apple.com/legal/contact and select from the drop-down menu provided. To report suspected counterfeit or knockoff products, or other forms of suspected infringement of Apple intellectual property, select Counterfeits & Knockoffs from the drop-down menu.
Corporate Address
Apple
One Apple Park Way
Cupertino, CA 95014
(408) 996–1010
Frequently Requested Info
Apple ID Support

Learn more about getting an Apple ID and its benefits.

Learn more
AppleCare Products

Find out how to get additional technical support and hardware service options for your Apple products.

Learn more
Repair and Service

See all your repair and service options based on your product and location.

Learn more
Apple Support Communities

Give and get help and tips from thousands of other Apple customers.

Learn more
Repair Status

Quickly and easily get the status of one or all of your repairs.

Learn more
Job Opportunities

Find current openings, college jobs, internships, and more.

Learn more
Media and Analyst Info

Get press releases, media contacts, and more.

Learn more
Email Subscriptions

Update your email address or change your subscription status.

Learn more
User Groups

Mix and mingle with other Apple Users in your area.

Learn more
Feedback

Tell us how we’re doing. Select the appropriate feedback option (we read everything, but can’t always respond):

Product Feedback

Website Feedback

Developer Feedback
Apple Footer
 Apple

    Contacting Apple

Shop and Learn

    Store
    Mac
    iPad
    iPhone
    Watch
    AirPods
    TV & Home
    AirTag
    Accessories
    Gift Cards

Services

    Apple Music
    Apple TV+
    Apple Fitness+
    Apple News+
    Apple Arcade
    iCloud
    Apple One
    Apple Card
    Apple Books
    Apple Podcasts
    App Store

Account

    Manage Your Apple ID
    Apple Store Account
    iCloud.com

Apple Store

    Find a Store
    Genius Bar
    Today at Apple
    Apple Camp
    Apple Store App
    Refurbished and Clearance
    Financing
    Apple Trade In
    Order Status
    Shopping Help

For Business

    Apple and Business
    Shop for Business

For Education

    Apple and Education
    Shop for K-12
    Shop for College

For Healthcare

    Apple in Healthcare
    Health on Apple Watch
    Health Records on iPhone

For Government

    Shop for Government
    Shop for Veterans and Military

Apple Values

    Accessibility
    Education
    Environment
    Inclusion and Diversity
    Privacy
    Racial Equity and Justice
    Supplier Responsibility

About Apple

    Newsroom
    Apple Leadership
    Career Opportunities
    Investors
    Ethics & Compliance
    Events
    Contact Apple

More ways to shop: Find an Apple Store or other retailer near you. Or call 1-800-MY-APPLE.
United States
Copyright © 2022 Apple Inc. All rights reserved.
Privacy Policy Terms of Use Sales and Refunds Legal Site Map

            ''' 


phoneNumberRegex = re.compile(r'''(
            (\d{3}|\(\d{3}\))         #area code
            (-|.| )?                  #seperator
            (\d{3})                   #first 3 digits
            (-|.)?                    #seperator
            (\d{3})                   #last 4 digits
                                  )''', re.VERBOSE)


emailRegex = re.compile(r'''(
            [a-zA-Z0-9.+_]+
            @
            [a-zA-Z0-9.]+
            \.
            [a-zA-Z]{2,4}
                            )''', re.VERBOSE)

numbers = ''
emails = ''
match_n = []
for group in phoneNumberRegex.findall(searchText2):
    match_n.append(group[0])
match_e = emailRegex.findall(searchText2)

numbers = '\n'.join(match_n)
emails = '\n'.join(match_e)

if not numbers and not emails:
    print ('The text does not contain any phone numbers or email addresses.')
elif not numbers and emails:
    print ('The text does not contain any phone numbers.\n\nThe emails in the text are:\n'+emails)
elif not emails and numbers:
    print ('The text does not contain any email addresses.\n\nThe phone numbers in the text are:\n'+numbers)
else:
    print ('The phone numbers in the text are:\n'+numbers+'\n\nAnd the emails in the text are:\n'+emails)