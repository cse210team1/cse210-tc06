import random

class Board:


    def __init__(self):

        self.keyword = []
        for i in range(4):
            self.keyword.append(random.randint(0,9))

        self.feedback = []
        self.finished_feedback = ["X","X","X","X"]

    def apply(self, guess):
        self.feedback.clear()
        for i in range(len(str(guess))):
            guess = str(guess)
            # print(f"keyword list: {self.keyword} feedback: {self.feedback} guess: {guess}" )
            # print(f"guess:{guess[i]} keyword: {self.keyword[i]}")
            if int(guess[i]) == self.keyword[i]:
                self.feedback.append("X")
            elif int(guess[i]) in self.keyword:
                self.feedback.append("O")
            else:
                self.feedback.append("*")

    def is_solved(self):
        return (self.feedback == self.finished_feedback )
        

    def to_string(self, current_player):
        text =  "\n--------------------"
        text += "\n" + str(current_player) + ": "
        if len(self.feedback) == 0:
            text += "----"
        else:
            for symbol in self.feedback:
                text += symbol
        text += "\n--------------------"
        return text
        
            
    def clear_feedback(self):
        self.feedback.clear()