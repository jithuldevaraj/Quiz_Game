from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Creating a question object List.
question_bank = []
for question in question_data:
    temp_question_obj = Question(question["text"], question["answer"])  # Creating a Question Object.
    question_bank.append(temp_question_obj)  # Append each question object to question_bank list.

obj_quiz_brain = QuizBrain(question_bank)
while obj_quiz_brain.still_has_questions():
    obj_quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {obj_quiz_brain.score}/{obj_quiz_brain.question_number}")
