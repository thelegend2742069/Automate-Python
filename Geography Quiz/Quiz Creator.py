"""
Say you're a geography teacher with 35 students in your class and you want
to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in
it, and you can't trust the students not to cheat. You'd like to randomize the
order of questions so that each quiz is unique, making it impossible for any-
one to crib answers from anyone else. Of course, doing this by hand would
be a lengthy and boring affair. Fortunately, you know some Python.


Here is what the program does:
    Creates 35 different quizzes.
    Creates 50 multiple-choice questions for each quiz, in random order.
    Provides the correct answer and three random wrong answers for each question, in random order.
    Writes the quizzes to 35 text files.
    Writes the answer keys to 35 text files.


This means the code will need to do the following:
    Store the states and their capitals in a dictionary.
    Call open(), write(), and close() for the quiz and answer key text files.
    Use random.shuffle() to randomize the order of the questions and multiple-choice options.

"""


import random, os


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


states = list(capitals.keys())
wrongOptions = []


for i in range(1,36):
    quizFile = open('Quiz '+str(i)+'.txt', 'w')
    random.shuffle(states)      #shuffle the states

    for j in range(0,50):
        quizFile.write('Question '+str(j+1)+':\nWhat is the capital of '+states[j]+'?\n')       #write the question
        
        wrongOptions = list(capitals.values())                          #create list of wrong options 
        wrongOptions.remove(capitals[states[j]])                        #remove correct option
        #print(wrongOptions)
        options = random.sample(wrongOptions, 3)                        #add 3 wrong options and correct option
        options.append(capitals[states[j]])
        random.shuffle(options)
        
        #write the options
        quizFile.write('a. %s\nb. %s\nc. %s\nd. %s\n\n' % (options[0], options[1], options[2], options[3]))
    
    quizFile.close()
    
    answerKey = open('Answer Key '+str(i)+'.txt', 'w')                  #create answer key file
    answerKey.write('Answers to Quiz %s are:\n\n' %(str(i)))

    for l in range(0,50):                                               #write answers to each question
        answerKey.write('Question '+str(l+1)+': '+capitals[states[l]]+'\n\n') 
    
    answerKey.close()
    print('Quiz %s created.\n' % (str(i)))