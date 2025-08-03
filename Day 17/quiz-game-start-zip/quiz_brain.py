#quizbrain class
class QuizBrain:

    def __init__(self,  q_list):
        """ Initializes the QuizBrain with a list of questions. """
        self.q_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_questions_left(self):
        """ Returns True if there are still questions left to ask, else False."""

        #if question number is less then the total questions length the loop will continue in main.py else it will break
        if self.q_number < len(self.questions_list):
            return True
        else:
            return False

    def next_question(self):
        """ Presents the next question to the user and gets their answer.
        Returns:
            str: The user's answer input."""
        #saves question from list on q_number index
        quiz_question = self.questions_list[self.q_number]

        #increases the q_number by 1
        self.q_number += 1

        #saves the answer for user input
        #quiz_question.text = retrieves only the "text" from question list dict
        u_answer = input(f"Q{self.q_number}: {quiz_question.text} (True/False): ")

        return u_answer

    def validation(self,u_answer):
        """ Validates the user's answer against the correct answer.
        Updates the score if correct.
        Args:
            u_answer (str): The user's answer input.
        Returns:
            bool: True if the answer is correct, else False."""

        #-1 because in next question we add +1 in q_number if that continues the answer will match the next question's index
        quiz_answer = self.questions_list[self.q_number - 1]

        #saves the answer from dict
        answer = quiz_answer.answer

        #validating answer conditions
        if u_answer.lower() == answer.lower():
            print("You got it Right!\n")
            self.score += 1
            return True
        else:
            print("That's the wrong\n")
            print(f"The correct answer was: {answer}")
            return False


    def get_score(self):
        """Returns the score"""
        return self.score
