from question_model import Questions
from quiz_brain import QuizBrain
from data import question_data


if __name__ == "__main__":
    # gnerate question bank
    question_bank = []
    for i in range(len(question_data)):
        question_bank.append(Questions(question_data[i]["question"], question_data[i]["correct_answer"]))

    quiz_brain = QuizBrain(question_bank)
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()

    print("You've completed the quiz")
    print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}")
