# Chapter X problem VIII Trivia game by Vincenzo Scotto Di Uccio

class Trivia:
    def __init__(self,question, ans1, ans2, ans3, ans4, cor_ans):
        self.__question = question
        self.__answer1 = ans1
        self.__answer2 = ans2
        self.__answer3 = ans3
        self.__answer4 = ans4
        self.__correct_answer = cor_ans

    def get_question(self):
        return self.__question
    
    def get_answer(self):
        return self.__correct_answer

    def __str__(self):
        return ("Question: " + str(self.__question) + "\n"
                "1) " + str(self.__answer1) + "\n"
                "2) " + str(self.__answer2) + "\n"
                "3) " + str(self.__answer3) + "\n"
                "4) " + str(self.__answer4) + "\n")


