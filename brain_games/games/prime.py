from random import randint
import math

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(num):
    mx = math.sqrt(num)
    for i in range(2, int(mx) + 1):
        if num % i == 0 or num == 1:
            return False
    return True


def game_logic():
    question = randint(1, 100)
    answer = 'yes' if prime(question) else 'no'
    return (question, answer)
