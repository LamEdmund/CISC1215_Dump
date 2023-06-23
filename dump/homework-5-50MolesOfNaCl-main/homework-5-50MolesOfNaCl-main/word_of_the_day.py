import datetime
import random

#takes in string for file name, returns populated dictionary
def generate_dict(fileN):
    newDict = {}
    ## append key value pair to dictionary with keys being ascii dec codes 97-122 value being an empty list
    for i in range(97, 123):
        newDict[chr(i)] = []

    #populate dictionary
    file = open(fileN)
    for line in file:
        newDict[line[0]].append(line.strip()) # identify key by first char in the line and append line to list
    file.close()
    return newDict

#takes in int for day and returns a string
def get_word_of_the_day(day):
    wordDict = generate_dict("words.txt")
    # ensure day is within range of 26
    if day <= 26:
        day = day - 1
    else:
        day = (day % 26)-1

    #get list with key with index day, since it is already ordered
    #return randomly selected element from given list
    return random.choice(wordDict[list(wordDict.keys())[day]])
    
if __name__ == '__main__':
    #print(get_word_of_the_day(1))
    print(get_word_of_the_day(datetime.datetime.today().day))
