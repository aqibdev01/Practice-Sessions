from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    # Apply the best practice without for loop
    a = questions["category"]
    b = questions["type"]
    c = questions["difficulty"]
    d = questions["question"]
    e = questions["correct_answer"]
    exam = Question(d,e,a,b,c)
    question_bank.append(exam)

qb = QuizBrain(question_bank)


while qb.still_has_questions():
    qb.next_question()

print("You have completed the quiz")
print(f"Your final score is {qb.score}/{qb.question_number}")