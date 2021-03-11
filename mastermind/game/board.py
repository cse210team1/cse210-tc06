import random

class Board:


    def __init__(self):

        self.keyword = []
        for i in range(4):
            self.keyword.append(random.randint(0,9))

        self.feedback = []

    def apply(self, guess):
        for i in range(len(geuss)):
            if str(guess)[i] == self.keyword[i]:
                feedback.append("x")
            elif str(guess)[i] in self.keyword:
                feedback.append("o")
            else:
                feedback.append("*")

    def is_solved(self, guess):
        return (self.feedback == self.keyword)
        

    def to_string(self, current_player):
        text =  "\n--------------------"
        text += current_player + ": "
        if len(self.feedback == 0):
            text += "----"
        else:
            for symbol in self.feedback:
                text += symbol

        for symbol in self.display:
            text += symbol
        text += "\n--------------------"
        return text
        
            
    def clear_feedback(self):
        self.feedback = []