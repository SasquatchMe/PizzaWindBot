from dataclasses import dataclass, field

import requests


def get_questions_from_api():
    geos = requests.get("http://main-app:8000/geopos/random/5").json()
    # geos = requests.get("http://localhost:8000/geopos/random/5").json()
    return geos


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
    location: tuple[float, float]

    correct_answer: str = field(init=False)

    def __post_init__(self):
        self.correct_answer = next(
            answer.text for answer in self.answers if answer.is_correct
        )


def map_question_answer(data):
    result = []

    for geopos in data:
        answers = []
        coord = (geopos["latitude"], geopos["longitude"])
        q_text = geopos["questions"]["text"]

        for answer in geopos["questions"]["answers"]:
            answers.append(Answer(text=answer["text"], is_correct=answer["is_correct"]))

        result.append(Question(text=q_text, answers=answers, location=coord))

    return result


def get_questions():
    questions = map_question_answer(get_questions_from_api())
    return questions
