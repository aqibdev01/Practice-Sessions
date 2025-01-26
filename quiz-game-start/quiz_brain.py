class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        for i in range(len(self.question_list)):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Type: {current_question.type}\n{current_question.category} {current_question.difficulty}\nQ {self.question_number}. {current_question.text} (True/False) ")
            self.check_answer(user_answer, current_question.answer)
            
        else:
            exit()
    
    def check_answer(self, coming, actual):
        if coming.lower() == actual.lower():
            self.score += 1
            print("You got it right!")
            
        else:
            print("Wrong Answer")
        print(f"Correct answer is {actual}")
        print(f"Your current score is: {self.score}/{self.question_number}")