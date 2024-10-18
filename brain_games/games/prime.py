from random import randint
import math

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    mx = math.sqrt(num)
    if num < 2:
        return False
    for i in range(2, int(mx) + 1):
        if num % i == 0:
            return False
    else:
        return True


def game_logic():
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return (question, answer)
