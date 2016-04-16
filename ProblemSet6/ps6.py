import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story
WORDLIST_FILENAME = 'words.txt'





class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        self.encrypting_dict  = {}
        for letter in range (0-shift,26-shift):
            self.encrypting_dict [string.ascii_lowercase[letter]]= string.ascii_lowercase[letter+shift]
            self.encrypting_dict [string.ascii_uppercase[letter]]= string.ascii_uppercase[letter+shift]

        return self.encrypting_dict 

    def apply_shift(self, shift):
        message_text_encrypted = ""
        self.build_shift_dict(shift)
        for letter in self.message_text:
            message_text_encrypted += self.encrypting_dict.get(letter,letter)
            
        return message_text_encrypted






class PlaintextMessage(Message):
    def __init__(self, text, shift):
        self.shift = shift
        Message.__init__(self, text)
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift( shift)
    def get_shift(self):
        return self.shift

    def get_encrypting_dict(self):
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        if 0<= shift < 26:
            self.shift = shift
            self.encrypting_dict = self.build_shift_dict(shift)
            self.message_text_encrypted = self.apply_shift(shift)
                        

            
        

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best =0
        bestShift =26
        temp = self.message_text.split(" ")
        print self.message_text
        temp2 = self.message_text

        for i in range(26):
            count = 0

            temp2 = self.apply_shift( i)

            temp = temp2.split(" ")
            print temp , "      ",temp2
            for word in temp:
                
                if   word in self.valid_words:
                    print word
                    count +=1

                    
            if count>best:
                best = count
                bestShift = i

        self.message_text = self.apply_shift(bestShift)
        return bestShift,self.message_text
        

##print 'Expected Output: jgnnq'
##print 'Actual Output:', plaintext.get_message_text_encrypted()
##    
##ciphertext = CiphertextMessage('jgnnq')
##print 'Expected Output:', (24, 'hello')
##print 'Actual Output:', ciphertext.decrypt_message()


