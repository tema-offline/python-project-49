from random import randint
import math

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(num):
    mx = math.sqrt(num)
    i = 2
    while i <= mx:
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def run_game():
    question = randint(0, 100)
    answer = 'yes' if prime(question) else 'no'
    return (question, answer)
