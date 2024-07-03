# Name: Daniel Reid Nelsen
# Class: CS 372 Intro to Networking
# Project: Portfolio Project 
# Due: 12/7/2023
# Description:  This is the Trivia class for the trivia game that is contained 
#               in the server.py file.  

import random
import json

# Trivia Database adapted from Open-trivia-database
# 5,484 questions are concatenated into the trivia_questions.json file
# https://github.com/el-cms/Open-trivia-database
# Accessed 12/2/2023

class TriviaGame():
    
    def __init__(self):
        self.numQuestions = 0
        self.numRight = 0
        self.currentQuestion = ""
        self.currentAnswer = ""
        self.questionList = []
        self.numAnswered = 0

    def getQuestion(self):
        '''
        Returns current question being asked.

        return: self.currentQuestion
        '''

        return self.currentQuestion
    
    def getScore(self):
        '''
        Retrieve the current score percentage

        return: float of number questions answered right divided by number of 
                questions asked
        '''

        # making sure that the program isn't dividing by zero if the game 
        # starts but quits before answering any question
        if self.numAnswered == 0:
            self.numAnswered = 1

        return (self.numRight / self.numAnswered) * 100
    
    def getNumRight(self):
        '''
        return: number of correctly answered questions
        '''

        return self.numRight
    
    def getNumAnswered(self):
        '''
        return: number of answered questions
        '''

        return self.numAnswered

    def setQuestionAndAnswer(self):
        '''
        Gets a random question from the list of trivia questions and puts in
        the class variable self.currentQuestion and self.currentAnswer
    
        return: nothing
        '''

        randQuestion = random.randint(0, self.numQuestions)
        
        self.currentQuestion = self.questionList[randQuestion]["question"]
        self.currentAnswer = str(self.questionList[randQuestion]["answers"]).strip("['").strip("']")

    def readQuestionsFromFile(self):
        '''
        Opens and reads trivia questions from trivia_questions.json file. Sets
        self.questionList dictionary with these questions and self.numQuestions 
        with the number of questions in the dictionary

        return: nothing
        '''

        # Read JSON file using Python
        # https://www.geeksforgeeks.org/read-json-file-using-python/
        # Accessed: 12/2/2023
        f = open('trivia_questions.json')
        
        self.questionList = json.load(f)
        self.numQuestions = len(self.questionList)

    def checkAnswer(self, answer):
       '''
        checks inputted answer with answer from the question list

        Increments self.numAnswered 

        return: Bool - True is correct
       '''
       
       self.numAnswered += 1
        
       if answer.lower() == self.currentAnswer.lower():
            self.numRight += 1
            return True


if __name__ == "__main__":
    game = TriviaGame()
