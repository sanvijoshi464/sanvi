import random

class QuizGame:
    def __init__(self, questions):
        """
        Initialize the QuizGame with a list of questions.
        Each question is a dictionary with 'question', 'options', and 'correct_answer'.
        """
        self.questions = questions
        self.score = 0

    def display_question(self, question_number):
        """
        Display a question along with multiple-choice options.
        """
        question = self.questions[question_number]['question']
        options = self.questions[question_number]['options']

        print(f"\nQuestion {question_number + 1}: {question}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    def get_user_input(self):
        """
        Get user input for the answer and validate it.
        """
        while True:
            try:
                user_input = int(input("\nEnter your choice (1-4): "))
                if 1 <= user_input <= 4:
                    return user_input
                else:
                    print("Please enter a valid option (1-4).")
            except ValueError:
                print("Please enter a valid number.")

    def evaluate_answer(self, question_number, user_answer):
        """
        Evaluate the user's answer and provide feedback.
        Update the score accordingly.
        """
        correct_answer = self.questions[question_number]['correct_answer']
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    def run_quiz(self):
        """
        Run the entire quiz, displaying questions, getting user input, and evaluating answers.
        Display the final score at the end.
        """
        for i in range(len(self.questions)):
            self.display_question(i)
            user_answer = self.get_user_input()
            self.evaluate_answer(i, user_answer)

        print(f"\nQuiz Completed! Your final score is: {self.score}/{len(self.questions)}")

# Example Quiz Questions
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'correct_answer': 3
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'correct_answer': 1
    },
    {
        'question': 'Who wrote Romeo and Juliet?',
        'options': ['Charles Dickens', 'William Shakespeare', 'Jane Austen', 'Mark Twain'],
        'correct_answer': 2
    }
]

# Create and run the quiz
if __name__ == "__main__":
    my_quiz = QuizGame(quiz_questions)
    my_quiz.run_quiz()
