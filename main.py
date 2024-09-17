from question_model import Question
from data import question_data

# Create a question object
question_bank = []
for question in question_data:
    temp_question_obj = Question(question["text"], question["answer"])  # Creating a Question Object.
    question_bank.append(temp_question_obj)  # Append each question object to question_bank list.

print(question_bank[0].text) 
print(question_bank[0].answer)




