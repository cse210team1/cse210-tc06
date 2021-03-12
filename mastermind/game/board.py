import random

class Board:


    def __init__(self):

        self.keyword = []
        for i in range(4):
            self.keyword.append(random.randint(0,9))

        self.feedback = []

    def apply(self, guess):
        for i in range(len(str(guess))):
            if str(guess)[i] == self.keyword[i]:
                self.feedback.append("x")
            elif str(guess)[i] in self.keyword:
                self.feedback.append("o")
            else:
                self.feedback.append("*")

    def is_solved(self):
        return (self.feedback == self.keyword)
        

    def to_string(self, current_player):
        text =  "\n--------------------"
        text += "\n" + str(current_player) + ": "
        if len(self.feedback) == 0:
            text += "----"
        else:
            for symbol in self.feedback:
                text += symbol
        text += "\n--------------------"
        print(self.feedback)
        return text
        
            
    def clear_feedback(self):
        self.feedback = []