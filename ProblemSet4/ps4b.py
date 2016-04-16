from ps4a import *
import time


def compChooseWord(hand, wordList, n):
   
    maxScore= 0

    maxWord = ""
    for word in wordList:
        if isValidWord(word, hand, wordList)==True:
            tempScore = getWordScore(word, n)
            if maxScore<tempScore:
                maxScore= tempScore
                maxWord=word
    if maxWord=="":
        return None
    return maxWord


def compPlayHand(hand, wordList, n):

    totalScore=0
    while calculateHandlen(hand)!=0:
        print
        print "Current Hand:",
        displayHand(hand)        
        word = compChooseWord(hand, wordList, n)        
        if word=="." :
            print "Goodbye! Total score:",totalScore, "points. "
            return
        else:
            if word==None:
                print "Total score:",totalScore, "points. "
                print
                return
            else:
                temp = getWordScore(word, n)
                totalScore+=temp
                print    '"'+word+'"','earned ',temp,' points. Total: ',totalScore,' points.'
                hand = updateHand(hand, word)
    print 'Run out of letters. Total: ',totalScore,' points.'
    print
    
def playGame(wordList):
    print "playGame not yet implemented." 
    lastHand={}
    n= HAND_SIZE
    hand = None
    boolea=False
    while     boolea==False:
        choose=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        print
        if choose=="n":
            lastHand= dealHand(n)
            playHand(lastHand, wordList, n)        
        elif choose=="r" :
            if lastHand!={}:
                playHand(lastHand, wordList, n)
            else:
                print "You have not played a hand yet. Please play a new hand first!"
                print
        elif choose=="e":
            return
        else:
            print "Invalid command."
            print 
            
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)




    
