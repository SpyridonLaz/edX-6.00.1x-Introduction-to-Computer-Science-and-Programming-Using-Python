from ps4b import *
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList


def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def getWordScore(word, n):
    summary = 0
    bonus =0
    for i in range(len(word)):
        summary+= SCRABBLE_LETTER_VALUES[word[i]]
    if len(word)==n:
        bonus =50
    return summary*len(word) + bonus




def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,      
    print                      

def dealHand(n):
    hand={}
    numVowels = n / 3
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


def updateHand(hand, word):
    tempHand=hand.copy()
    for letter in word:
        tempHand[letter] = tempHand.get(letter,0) - 1
    return tempHand


def isValidWord(word, hand, wordList):
        tempHand=hand.copy()
        for letter in word:
                tempHand[letter] = tempHand.get(letter,0) - 1
                if tempHand[letter] <0:
                        return False
        if word in wordList:
                return True
        else:
                return False

def calculateHandlen(hand):

    counter=0
    for i in hand:
        counter+=hand.get(i,0)
    return counter



def playHand(hand, wordList, n):
    totalScore=0
    while calculateHandlen(hand)!=0:
        print "Current Hand:",
        displayHand(hand)
        word = raw_input("Enter word, or a '.' to indicate that you are finished:")
        print
        
        if word=="." :
            print "Goodbye! Total score:",totalScore, "points. "
            return
        else:
            if isValidWord(word, hand, wordList)!=True:
                print "Invalid word, please try again."
                print
            else:
                temp = getWordScore(word, n)
                totalScore+=temp
                print    '"'+word+'"','earned ',temp,' points. Total: ',totalScore,' points.'
                print   
                hand = updateHand(hand, word)                
    print 'Run out of letters. Total: ',totalScore,' points.'
    print
    
    


def playGame(wordList):
    lastHand={}
    n= HAND_SIZE
    hand = None
    while   True:
        choose=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        print
        if choose=="r"or choose == "n":


            if choose=="r" and lastHand=={} :
                print "You have not played a hand yet.Please play a new hand first!"
                print
                continue

            while True: 

                compChoose=raw_input("Enter u to have yourself play, c to have the computer play: ")
                print

                if compChoose == "c" or compChoose == "u" :                                   
                        if  choose=="n":
                                lastHand = dealHand(n)
                                if compChoose == "c":
                                                compPlayHand(lastHand, wordList, n)
                                                break
                                else:
                                        playHand(lastHand, wordList, n)
                                        break
                        elif  choose=="r":
                                
                                if compChoose == "c":
                                        compPlayHand(lastHand, wordList, n)
                                        break

                                else:
                                        playHand(lastHand, wordList, n)
                                        break
                else:
                    print "Invalid command."
                    print  
                                            
                                
        elif choose=="e":
            return
        else:
            print "Invalid command."
            print          



if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
