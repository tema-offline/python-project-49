import random
import prompt
from brain_games.cli import welcome_user

RULES = 'What number is missing in the progression?'


def progression_game():
    player_name = welcome_user()
    quanity = 0
    print(RULES)
    while quanity < 3:
        step = random.randint(1, 10)
        start = random.randint(1, 100)
        stop = start + (step * 10)
        progression = [str(x) for x in range(start, stop, step)]
        skip = random.randint(0, 9)
        answer = progression[skip]
        progression[skip] = ".."
        question = " ".join(progression)
        print(f'Question: {question}')
        player_answer = prompt.string("Your answer: ")
        if player_answer != str(answer):
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {player_name}!")
            break
        else:
            print('Correct!')
        quanity += 1
    if quanity == 3:
        print(f'Congratulations, {player_name}!')


def main():
    progression_game()


if __name__ == "__main__":
    main()
