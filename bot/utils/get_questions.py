from dataclasses import dataclass, field

import requests


def get_questions_from_api():
    questions = requests.get('http://main-app:8000/questions').json()
    return questions[:5]


@dataclass
class Answer:
    """
    Represents an answer to a question.
    """

    text: str
    """The answer text"""
    is_correct: bool = False
    """Indicates if the answer is correct"""


@dataclass
class Question:
    """
    Class representing a quiz with a question and a list of answers.
    """

    text: str
    """The question text"""
    answers: list[Answer]
    """List of answers"""

    correct_answer: str = field(init=False)

    def __post_init__(self):
        self.correct_answer = next(answer.text for answer in self.answers if answer.is_correct)


def map_question_answer(data):
    result = []

    for question in data:
        answers: list[Answer] = []
        for answer in question['answers']:
            answers.append(Answer(text=answer['text'], is_correct=answer['is_correct']))
        result.append(Question(text=question['text'], answers=answers))
    return result


def get_questions():
    questions = map_question_answer(get_questions_from_api())
    return questions
