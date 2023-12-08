import random


class CharivnaKulka:

    class AnswerExistsException(Exception):
        pass

    class AnswerNotExistsException(Exception):
        pass

    DEFAULT_PROBABILITY: float = 1.0

    def __init__(self):
        self.__answers: dict[str, float] = {
            'Yes': CharivnaKulka.DEFAULT_PROBABILITY,
            'No': CharivnaKulka.DEFAULT_PROBABILITY,
            'Maybe': CharivnaKulka.DEFAULT_PROBABILITY,
        }

    def __chose_random_answer(self) -> str:
        return random.choices(
            list(self.__answers.keys()),
            list(self.__answers.values())
        )[0]

    def predict(self, question: str) -> str:

        if not isinstance(question, str):
            raise TypeError('Question type must be string!')

        answer = self.__chose_random_answer()

        print(f'You asked Kulka: {question}')
        print(f'[Kulka]: {answer}')

        return answer

    def add_answer(self, answer: str, probability: float = None):

        if not isinstance(answer, str):
            raise TypeError('Answer type must be string!')

        if probability is None:
            probability = CharivnaKulka.DEFAULT_PROBABILITY

        if not isinstance(probability, float):
            raise TypeError('Probability type must be float!')

        if answer in self.__answers.keys():
            raise CharivnaKulka.AnswerExistsException('Answer already exists!')

        self.__answers[answer] = probability

    def remove_answer(self, answer: str):

        if not isinstance(answer, str):
            raise TypeError('Answer type must be string!')

        if answer not in self.__answers.keys():
            raise CharivnaKulka.AnswerNotExistsException('Answer not exists!')

        del self.__answers[answer]