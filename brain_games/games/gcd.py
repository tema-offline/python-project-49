from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(rand_1, rand_2, rand_3):
    count = 0
    for i in range(1, rand_3 + 1):
        if rand_1 % i == 0 and rand_2 % i == 0:
            count = i
    return count


def game_logic():
    randint_1 = randint(1, 100)
    randint_2 = randint(1, 100)
    randint_3 = min(randint_1, randint_2)
    question = f"{randint_1} {randint_2}"
    answer = get_gcd(randint_1, randint_2, randint_3)
    return (question, answer)
