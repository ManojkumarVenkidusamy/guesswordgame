import random
import getpass

class GuessWord(object):
    
    def __init__(self,game_word):
		self.word=game_word
        
    def start_game(self):
        while True:
            self.star = 0
            self.exc = 0
            self.tmp_word_length = 0
            self.same_index = []
            self.diff_index = []

            #grabbing the guess word and checking the word length
            while self.tmp_word_length != len(self.word):
                self.tmp_word = raw_input("\nEnter your guess that must be containing "+ str(len(self.word)) +" letters: ")
                self.tmp_word_length = len(self.tmp_word)

            #Exact word match if block
            if self.word == self.tmp_word:
                self.new_key = int(raw_input("\nCongrats! you've got the right word. To continue playing the game please enter 1 and to quit enter 2: \n 1. play \n 2. quit \n"))
                if self.new_key == 1:
                    #self.last_word.append(self.word)
                    self.word = getpass.getpass("Player1 Please enter the word for player2 to guess : ")
                    continue
                else:
                    print "Thank you for playing..Play again..."
                    break

            #star calculation
            self.calculate_star()

            #Exclamation calculation
            for i in range(len(self.word)):
                for j in range(len(self.tmp_word)):
                    if i != j and self.tmp_word[i] == self.word[j] and self.tmp_word[i] not in self.same_index and self.tmp_word[i] not in self.diff_index:
                                self.diff_index.append(self.tmp_word[i])
                                self.exc +=1
            #Guess output
            print ' '.join(['_' for i in range(len(self.word))]) + '\t' + ' '.join(['*' for i in range(self.star)]) + ' '.join([' !' for i in range(self.exc)])

    def calculate_star(self):
        for i in range(len(self.word)):
            if self.tmp_word[i] == self.word[i]:
                self.same_index.append(self.tmp_word[i])
                self.star += 1

 