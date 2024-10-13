from random import randint, choice
from operator import add, sub, mul

RULES = 'What is the result of the expression?'
symbols = [("+", add), ("-", sub), ("*", mul)]


def run_game():
    randint_1 = randint(1, 100)
    randint_2 = randint(1, 100)
    operator, func = choice(symbols)
    question = f"{randint_1} {operator} {randint_2}"
    answer = func(randint_1, randint_2)
    return (question, answer)
