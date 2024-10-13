from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def run_game():
    randint_1 = randint(1, 100)
    randint_2 = randint(1, 100)
    randint_3 = min(randint_1, randint_2)
    question = f"{randint_1} {randint_2}"
    answer = 0
    for i in range(1, randint_3 + 1):
        if randint_1 % i == 0 and randint_2 % i == 0:
            answer = i
    return (question, answer)
