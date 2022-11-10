import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_have_question(self):
        return self.question_number < len(self.question_list)
        # ^^^ FAJNY SPOSOB ^^^

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"{html.unescape(current_question.text)}"
        # self.check_answer(u_answer, current_question.answer)

    def check_answer(self, u_answer):
        if u_answer == self.question_list[self.question_number - 1].answer:
            self.score += 1
            return True
        else:
            return False


