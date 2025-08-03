from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#list for question objects
question_bank = []

for question in question_data:
    #retrives text and answer from question data list
    question_text = question["text"]
    question_answer = question["answer"]

    #saves the text and answer in objects new_question
    new_question = Question(question_text, question_answer)

    #appends new_question object (Carrying text and answer) to question bank list
    question_bank.append(new_question)

#creates object for quiz brain class and passes the quesiton bank list
quiz = QuizBrain(question_bank)

final_score = 0

while quiz.still_questions_left():

    #calls new question and saves user guess in answer
    answer = quiz.next_question()

    #calls validation function for validating answer
    quiz.validation(answer)

#prints the final score
print("You've completed the QUIZ.")
print(f"Your Final Score is: {quiz.get_score()}")
