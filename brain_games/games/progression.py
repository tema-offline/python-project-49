from random import randint

RULES = 'What number is missing in the progression?'


def game_logic():
    step = randint(1, 10)
    start = randint(1, 100)
    stop = start + (step * 10)
    progression = [str(x) for x in range(start, stop, step)]
    skip = randint(0, 9)
    answer = progression[skip]
    progression[skip] = ".."
    question = " ".join(progression)
    return (question, answer)
