import re
import string
import random


class Hangman:
    allowed = list(string.ascii_letters) +list(string.punctuation[:25] + string.punctuation[:26] + " ")
    def __init__(self, string=None, dictionary=None):
        if string:
            self.string = string
            self.dis = "".join(["_" if i != " " and i.isalpha() else (i if i != " " else " ") for i in string])
        if dictionary:
            with open(dictionary, "r") as f:
                words = f.read().split("\n")
                random.shuffle(words)
                self.string = words[0]
                self.dis = "".join(["_" if i != " " and i.isalpha() else (i if i != " " else " ") for i in self.string])
        self.guessed = []
        self.guess_wrong = []

    def checkLetter(self, letter):
        self.dis = self.dis.split()
        if letter.lower() not in self.guessed and letter.isalpha() and len(letter) == 1:
            total = 0

            self.guessed.append(letter.lower())
            string = self.string.split(" ")

            for x, word in enumerate(string):
                word = word.lower()
                total += word.count(letter.lower())
                for i in [i.start() for i in re.finditer(letter.lower(), word)]:
                    self.dis[x] = list(self.dis[x])
                    self.dis[x][i] = string[x][i]
                    self.dis[x] = "".join(self.dis[x])
            if total < 1: self.guess_wrong.append(letter)

        self.dis = " ".join(self.dis)

        return self.dis

    def checkWord(self, word):
        self.dis = self.dis.split()
        if word.lower() not in self.guessed:
            total = 0

            self.guessed.append(word.lower())
            string = self.string.split(" ")
            for i, w in enumerate(string):
                if word.lower() == w.lower():
                    total += 1
                    self.dis[i] = w

            if total < 1: self.guess_wrong.append(word)

        self.dis = " ".join(self.dis)

        return self.dis

    def checkFull(self, guess):
        if guess.lower() == self.string.lower():
            self.dis = self.string
            return self.string
        else:
            self.guess_wrong.append(guess)

    def check_win(self):
        if "_" not in list(self.dis):
            return True
        return False

    def hint(self):
        a = [i for i in self.string.lower() if i in list(string.ascii_lowercase) and i not in self.guessed]
        random.shuffle(a)
        self.checkLetter(a[0])
