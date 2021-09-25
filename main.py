from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [] #list of question obj
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    question_data = Question(q_text, q_answer)
    question_bank.append(question_data)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the challenge")
print(f"Your final score is {quiz.score}/{len(question_bank)}")

